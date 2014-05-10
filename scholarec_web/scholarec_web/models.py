from django.db import models
from django_facebook.models import FacebookProfileModel
from django.contrib.auth.models import UserManager
# Create your models here.

class MyCustomProfile(FacebookProfileModel):
    user = models.OneToOneField('auth.user')
    objects = UserManager()
    
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#Make sure we create a MyCustomProfile when creating a User
def create_facebook_profile(sender, instance, created, **kwargs):
    if created:
        MyCustomProfile.objects.create(user=instance)
        
post_save.connect(create_facebook_profile, sender=User)  
