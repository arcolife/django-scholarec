from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

def search(request):
    c = {}
    c.update(csrf(request))
    if request.POST:
        print request.POST['q']
        return HttpResponseRedirect("/")
    else:
        return render_to_response('search.html', c)

def test(request):    
    return render_to_response('test.html', {})
