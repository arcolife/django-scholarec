import urllib
import json
import pprint

#from pyes import *

#conn = ES('127.0.0.1:9200')

def build_query(search_term):
    q = { "query":{
        "bool":{
            "must":[{
                "query_string":{
                    "default_field":"_all",
                    "query":search_term
                }
            }],
            "must_not":[],
            "should":[]
        }},
          "from":0,
          "size":10,
          "sort":[],
          "facets":{}
      }
    
    return q

def __run_query(query, **kwargs):
    #query = build_query(str(query))
    #query = json.dumps(query)
    kwargs['q'] = query
    args = kwargs.keys()
    if 'search_size' in args:
        kwargs['size'] = kwargs.pop('search_size')
    else:
        kwargs['size'] = 10
    if 'search_from' in args:
        kwargs['from'] = kwargs.pop('search_from')
    else:
        kwargs['from'] = 0
    #query = '?q='+query+'&'
    query = urllib.urlencode(kwargs)
    #for key, value in kwargs.items():
    #    query+=key+'='+str(value)+'&'
    response = urllib.urlopen(
        'http://localhost:9200/arxiv/docs/_search?' + query
    )
    result = json.loads( response.read() )
    #pprint.pprint(result['hits']['hits'])
    
    #JE = json.encoder.JSONEncoder()
    #return JE.encode(result)
    return result

'''
def __ES_query(query):
    query = build_query(query)
    query = json.dumps(query)
    response = urllib.urlopen(
        'http://localhost:9200/arxiv/docs/_search',
        query
    )
    result = json.loads( response.read() )
    pprint.pprint(result['hits']['hits'])
    #JE = json.encoder.JSONEncoder()
    #return JE.encode(result)
    return result
'''
