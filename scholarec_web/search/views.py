from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

def search(request):
    c = {}
    c.update(csrf(request))
    #if request.POST:
    #     print request.POST['q'], "NOTHING"
    #     return HttpResponseRedirect("/")
    # else:
    return render_to_response('search_default.html', c, RequestContext(request))

def test(request):    
    return render_to_response('test.html', {})
