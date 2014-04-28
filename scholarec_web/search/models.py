from django.db import models
#from django.contrib.auth.models import User

'''
class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title
'''

'''
# post.models

class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    author = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    rating = models.IntegerField(choices=[(0, 'zero'), (1, 'one'), (2, 'two'),
        (3, 'three'), (4, 'four'), (5, 'five'), ], default=0)
'''
