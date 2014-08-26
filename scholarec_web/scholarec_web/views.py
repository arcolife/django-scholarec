# django specific
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
# app specific
import datetime
from dateutil.parser import parse
#from haystack.query import SearchQuerySet
from search import es_query
from users import control
#from users.models import History
from open_facebook import OpenFacebook
from django_facebook.api import get_persistent_graph
#import string
import json
from urllib import urlopen
import grequests

def home(request):    
    c = {}
    c.update(csrf(request))
    context = RequestContext(request)
    #print context
    return render_to_response('index.html', c, context)
    
def add(request):
    username = request.GET.get('username', None)
    p_id = request.GET.get('p_id', None)
    col_id = request.GET.get('col_id', None)
    title = request.GET.get('title', None)
    current = request.GET.get('current', None)
    q = request.GET.get('q', None)
    control.add_to_collection(username, col_id, p_id, title)
    return HttpResponseRedirect('/results/' + current + '?q=' + q)

def remove(request):
    username = request.GET.get('username', None)
    col_id = request.GET.get('col_id', None)
    current = request.GET.get('current', None)
    q = request.GET.get('q', None)
    control.remove_from_collection(username, col_id)
    return HttpResponseRedirect('/results/' + current + '?q=' + q)

def fav(request):
    username = request.GET.get('username', None)
    paper = request.GET.get('paper', None)
    current = request.GET.get('current', None)
    q = request.GET.get('q', None)
    rate = int(request.GET.get('rate', None))
    kw = request.GET.get('kw', None)
    print "FAVORITE req: username: %s paper_ID: %s Current_page: %s, Query: %s Rating: %s Keyword: %s " % \
        (username, paper, current, q, rate, kw)
    #table = string.maketrans("","")
    #kw = '%20'.join(kw.translate(table, string.punctuation).split())
    control.add_rating(username, paper, rate, q, kw)
    return HttpResponseRedirect('/results/' + current + '?q=' + q)

def profile(request):
    '''
    from django_facebook.api import get_facebook_graph, FacebookUserConverter, \
        get_persistent_graph, require_persistent_graph, get_user_attribute, \
        get_profile_model
    x = get_persistent_graph(request)
    #print require_persistent_graph(request)
    print dir(x.me)

    try:
        req = get_persistent_graph(request)
        graph = OpenFacebook(req.access_token)
        print "ME: ", graph.get('me')
    except:
        pass
    '''
    context = RequestContext(request)
    #x = context['user']

    '''
    #print graph.get('me')
    graph = request.user.get_offline_graph()
    print graph
    if graph:
        friends = graph.get('me/friends')
        print friends
    '''
    return render_to_response('profile.html', context)

def results(request, page):    
    query = request.GET.get('q', None)
    #print "page req: ", page
    #print SearchQuerySet().filter(content=query)
    #print "IN RESULTS: ", request.user #remember, user is an object
    if bool(query.split()):
        # add to search history
        history = control.add_to_history(query, str(request.user))
        if len(history) > 5:
            history = history[-5:]
        try:
            q_resp =  es_query.__run_query(query, search_from=int(page)-1, search_size=10)
            recos, favs = control.get_recommendations(str(request.user))
        except:
            return HttpResponse("Bad Request: Go back and check on your query parameters (mostly due to imbalanced \").")

        if bool(q_resp)==False:
            return HttpResponse('No results found! Go back')
            
        #print "\nQuery: %s" % (query)
        resp = []
        keywords = []
        _sources = q_resp['hits']['hits']
        for i in xrange(len(_sources)):
            temp = { 'title' : _sources[i]['_source']['title'],
                     #'authors' : '; '.join([j['name'] for j in _sources[i]['_source']['authors']]),
                     'authors' : [j['name'] for j in _sources[i]['_source']['authors']],
                     'summary' : _sources[i]['_source']['summary'],
                     'keyword' : _sources[i]['_source']['keyword'],
                     'published' : datetime.datetime.strptime(_sources[i]['_source']['published'], "%Y-%m-%dT%H:%M:%SZ"),
                     'ID' : _sources[i]['_source']['ID'],
                     'id' : _sources[i]['_id'],
                     'links' : [ {'href':j['href'],'type':j['type']} for j in _sources[i]['_source']['links']]
                     #'links' : '; '.join([j['href'] for j in _sources[i]['_source']['links']])
                 }
            
            keywords.append(_sources[i]['_source']['keyword'])
            resp.append(temp)
            
        return render_to_response('results.html', 
                                  { 'items' : resp, 
                                    'history' : history, 
                                    'collection' : control.get_collection(str(request.user)),
                                    'username' : str(request.user),
                                    'recommendations' : recos,
                                    'favorites' : favs,
                                    'total' : q_resp['hits']['total'],
                                    'took' : float(q_resp['took'])/1000, 
                                    'keywords' : list(set(keywords)),
                                    'current' : page,
                                    'q' : query })
    else:
        #return HttpResponse("No Query Sent!")
        return HttpResponseRedirect('/search/')

def record(request):
    doc_id = request.GET.get('doc', None)
    query = request.GET.get('q', None)
    try:
        response = urlopen('http://localhost:9200/arxiv/docs/'+ \
                           doc_id + '/_source')
    except:
        return HttpResponse('404: Not Found! Go back')
    result = json.loads(response.read())
    temp = []
    for a in result['authors']:
        temp.append(a['name'])
    result['authors'] = temp
    result['published'] = datetime.datetime.strptime(
        result['published'], "%Y-%m-%dT%H:%M:%SZ")
    return render_to_response('record.html', \
                              { 'item' : result,
                                'q' : query })

def authors(request):    
    return render_to_response('authors.html', {})

def citations(request):    
    return render_to_response('citations.html', {})

def references(request):    
    return render_to_response('references.html', {})

def publish_stats(request):    
    URL = "http://localhost:9200/arxiv/docs/_search"
    temp = """{
    "size": 0,
    "aggs": {
    "publish_stats": {
    "date_histogram": {
    "field": "published",
    "interval": "year"
    }}}}"""
    resp = grequests.map([grequests.post(URL, data=temp)])
    data = json.loads(resp[0].content)
    temp = data['aggregations']['publish_stats']['buckets']
    l = [['key_as_string', 'doc_count']]
    for i in temp:
        l.append([i[l[0][0]][:4],
                  #parse(i[l[0][0]]).strftime("%A,%e %B %G"),
                  i[l[0][1]]])
    return HttpResponse(json.dumps(l), content_type="application/json")

def keyword_stats(request):    
    URL = "http://localhost:9200/arxiv/docs/_search"
    temp = """{
    "size":0,
    "aggs":{
    "keyword_stats":{
    "terms":{
    "field":"keyword",
    "size": 200
    }}}}"""
    # "shard_size": 100 
    # Refer docs: ES search aggregations bucket terms aggregation
    resp = grequests.map([grequests.post(URL, data=temp)])
    data = json.loads(resp[0].content)
    temp = data['aggregations']['keyword_stats']['buckets']
    l = [['key', 'doc_count']]
    for i in temp:
        l.append([i[l[0][0]],
                  #parse(i[l[0][0]]).strftime("%A,%e %B %G"),
                  i[l[0][1]]])
    return HttpResponse(json.dumps(l), content_type="application/json")

def visualize(request):
    return render_to_response('viz.html')
