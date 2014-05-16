# django specific
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
# app specific
import datetime
from haystack.query import SearchQuerySet
from search import es_query
from users import control
#from users.models import History
from open_facebook import OpenFacebook
from django_facebook.api import get_persistent_graph

def home(request):    
    c = {}
    c.update(csrf(request))
    context = RequestContext(request)
    #print context
    return render_to_response('index.html', c, context)

def profile(request):
    '''
    from django_facebook.api import get_facebook_graph, FacebookUserConverter, \
        get_persistent_graph, require_persistent_graph, get_user_attribute, \
        get_profile_model
    x = get_persistent_graph(request)
    #print require_persistent_graph(request)
    print dir(x.me)
    '''
    try:
        req = get_persistent_graph(request)
        graph = OpenFacebook(req.access_token)
        print "ME: ", graph.get('me')
    except:
        pass
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
    print "page req: ", page
    #print SearchQuerySet().filter(content=query)
    #print "IN RESULTS: ", request.user #remember, user is an object
    if bool(query.split()):
        # add to search history
        history = control.add_to_history(query, str(request.user))
        if len(history) > 5:
            history = history[-5:]
        try:
            q_resp =  es_query.__run_query(query, search_from=int(page)-1, search_size=10)
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
                     #'keyword' : _sources[i]['_source']['keyword'],
                     'published' : datetime.datetime.strptime(_sources[i]['_source']['published'], "%Y-%m-%dT%H:%M:%SZ"),
                     'ID' : _sources[i]['_source']['ID'],
                     'links' : [ {'href':j['href'],'type':j['type']} for j in _sources[i]['_source']['links']]
                     #'links' : '; '.join([j['href'] for j in _sources[i]['_source']['links']])
                 }
            
            keywords.append(_sources[i]['_source']['keyword'])
            resp.append(temp)
            
        return render_to_response('results.html', 
                                  { 'items' : resp, 
                                    'history' : history, 
                                    'username' : str(request.user),
                                    'total' : q_resp['hits']['total'],
                                    'took' : float(q_resp['took'])/1000, 
                                    'keywords' : list(set(keywords)),
                                    'current' : page,
                                    'q' : query })
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

