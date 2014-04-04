from django.shortcuts import render_to_response
from haystack.query import SearchQuerySet
from search import es_query
from django.http import HttpResponseRedirect, HttpResponse

def home(request):    
    return render_to_response('index.html', {})

def results(request):    
    query = request.GET.get('q', None)
    #print SearchQuerySet().filter(content=query)
    if query:
        q_resp =  es_query.__run_query(query)
        if bool(q_resp)==False:
            return HttpResponse('No results found! Go back')

        print "\nQuery: %s" % (query)
        resp = []
        _sources = q_resp['hits']['hits']
        for i in xrange(len(_sources)):
            temp = { 'title' : _sources[i]['_source']['title'],
                     'authors' : '; '.join([j['name'] for j in _sources[i]['_source']['authors']]),
                     'summary' : _sources[i]['_source']['summary'],
                     'keyword' : _sources[i]['_source']['keyword'],
                     'published' : _sources[i]['_source']['published'],
                     'ID' : _sources[i]['_source']['ID'],
                     'links' : '; '.join([j['href'] for j in _sources[i]['_source']['links']])
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

