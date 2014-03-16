# app specific urls
from django.conf.urls import patterns, include, url
#from django.views.generic.simple import redirect_to
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from search import views

urlpatterns = patterns('',
                       #(r'^$', TemplateView.as_view(template_name="home.html")),
                       #(r'^test/', TemplateView.as_view(template_name="index.html")),
                       (r'^$', views.search),
                       (r'^test/$', views.test),
)
