from django.shortcuts import render_to_response
from haystack.query import SearchQuerySet
from search import es_query

def home(request):    
    return render_to_response('index.html', {})

def results(request):    
    query = request.GET.get('q', None)
    #print SearchQuerySet().filter(content=query)
    q_resp =  es_query.__run_query(query)
    print "\nQuery: %s" % (query)
    resp = []
    _sources = q_resp['hits']['hits']
    for i in xrange(len(_sources)):
        temp = { 'title' : str(_sources[i]['_source']['title']),
                 'authors' : str('; '.join([j['name'] for j in _sources[i]['_source']['authors']])),
                 'summary' : str(_sources[i]['_source']['summary']),
                 'keyword' : str(_sources[i]['_source']['keyword']),
                 'published' : str(_sources[i]['_source']['published']),
                 'ID' : str(_sources[i]['_source']['ID']),
                 'links' : str('; '.join([j['href'] for j in _sources[i]['_source']['links']]))
        }
        resp.append(temp)
        
    print resp[0]
    return render_to_response('results.html', { 'items' : resp })

def results_mod(request):    
    return render_to_response('results_mod.html', {})

def authors(request):    
    return render_to_response('authors.html', {})

def citations(request):    
    return render_to_response('citations.html', {})

def references(request):    
    return render_to_response('references.html', {})

