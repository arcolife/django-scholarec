from django.shortcuts import render_to_response

def index(request):    
    return render_to_response('index.html', {})

def results(request):    
    return render_to_response('results.html', {})

def authors(request):    
    return render_to_response('authors.html', {})

def citations(request):    
    return render_to_response('citations.html', {})

def references(request):    
    return render_to_response('references.html', {})

