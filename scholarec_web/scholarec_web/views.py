from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from haystack.query import SearchQuerySet
from search import es_query
from django.http import HttpResponseRedirect, HttpResponse
import datetime

def home(request):    
    c = {}
    c.update(csrf(request))
    context = RequestContext(request)
    #print context
    return render_to_response('index.html', c, context)

def profile(request):
    context = RequestContext(request)
    '''
    #print graph.get('me')
    graph = request.user.get_offline_graph()
    print graph
    if graph:
        friends = graph.get('me/friends')
        print friends
    '''
    return render_to_response('profile.html', context)

def results(request):    
    query = request.GET.get('q', None)
    #print SearchQuerySet().filter(content=query)
    print request.user
    if query:
        q_resp =  es_query.__run_query(query)
        if bool(q_resp)==False:
            return HttpResponse('No results found! Go back')

        print "\nQuery: %s" % (query)
        resp = []
        _sources = q_resp['hits']['hits']
        for i in xrange(len(_sources)):
            temp = { 'title' : _sources[i]['_source']['title'],
                     #'authors' : '; '.join([j['name'] for j in _sources[i]['_source']['authors']]),
                     'authors' : [j['name'] for j in _sources[i]['_source']['authors']],
                     'summary' : _sources[i]['_source']['summary'],
                     'keyword' : _sources[i]['_source']['keyword'],
                     'published' : datetime.datetime.strptime(_sources[i]['_source']['published'], "%Y-%m-%dT%H:%M:%SZ"),
                     'ID' : _sources[i]['_source']['ID'],
                     'links' : [ {'href':j['href'],'type':j['type']} for j in _sources[i]['_source']['links']]
                     #'links' : '; '.join([j['href'] for j in _sources[i]['_source']['links']])
                 }
            resp.append(temp)
            
        return render_to_response('results.html', { 'items' : resp })
    else:
        #return HttpResponse("No Query Sent!")
        return HttpResponseRedirect('/search/')

def results_mod(request):    
    return render_to_response('results_mod.html', {})

def authors(request):    
    return render_to_response('authors.html', {})

def citations(request):    
    return render_to_response('citations.html', {})

def references(request):    
    return render_to_response('references.html', {})

