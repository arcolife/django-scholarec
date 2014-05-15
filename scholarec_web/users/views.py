# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

from users.models import Poll, Choice

poll = Poll.objects(question__contains="What").first()
choice = Choice(choice_text="I'm at DjangoCon.fi", votes=23)
poll.choices.append(choice)
poll.save()

#print poll.question

def test(request):
    return HttpResponse("Poll: " + poll.question + " | Choice: "+ choice.to_json())
