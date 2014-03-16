from django.shortcuts import render_to_response

def search(request):
    d = {}
    return render_to_response('search.html', d)

def test(request):    
    return render_to_response('test.html', {})
