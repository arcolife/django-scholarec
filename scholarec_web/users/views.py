# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

def test(request):
    poll = Poll.objects(question__contains="What").first()
    choice = Choice(choice_text="I'm at my home", votes=22)
    #poll.choices.append(choice)
    #poll.save()
    #print poll.question
    return HttpResponse("Poll: " + poll.question + " | Choice: "+ choice.to_json())
