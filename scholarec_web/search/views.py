from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

def search(request):
    if request.POST:
        print request.POST['q']
        return HttpResponseRedirect("/")
    else:
        return render_to_response('search.html', {})

def test(request):    
    return render_to_response('test.html', {})
