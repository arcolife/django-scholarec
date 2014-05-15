# from django.db import models
from mongoengine import *

class Choice(EmbeddedDocument):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)

class Poll(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    choices = ListField(EmbeddedDocumentField(Choice))

    meta = {
        'indexes': [
            'question', 
            ('pub_date', '+question')
        ]
    }


""" form object like:
from users.models import Poll, Choice
>>> poll = Poll(question="What's new?", pub_date=timezone.now())
>>> choice = Choice(choice_text="I'm at DjangoCon.fi", votes=23)

>>> poll.choices.append(choice)
>>> poll.save()

"""
