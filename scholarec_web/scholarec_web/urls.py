## project wide urls
####################
from django.conf.urls import patterns, include, url
# from django.views.generic.simple import redirect_to
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib import admin
admin.autodiscover()
import settings
from django.conf import settings

## urls from each app
#####################
import search.urls
import users.urls
from scholarec_web import views
'''
from haystack.forms import HighlightedModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView
from search.models import Article

article_sqs = SearchQuerySet().models(Article)
'''
# Patterns
urlpatterns = patterns('',
                       # urls specific to this app
                       
                       # social_auth (pip installed)
                       #url(r'', include('social_auth.urls')),

                       url(r'test', include(users.urls)),
                       # social auth git example app
                       #url('', include('social.apps.django_app.urls', namespace='social')),
                       
                       url(r'search/', include(search.urls)),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       # catch all, redirect to search home view
                       
                       #url(r'^.*/$', TemplateView.as_view(template_name="home.html")),
                       #(r'^$', 'search.views.index'),
                       #(r'^$', TemplateView.as_view(template_name="index.html",
                       #                content_type='text/plain')),

                       (r'^facebook/', include('django_facebook.urls')),
                       (r'^accounts/', include('django_facebook.auth_urls')), 
                       
                       (r'^profile/?$', views.profile),
                       (r'^$', views.home),
                       (r'^results/(?P<page>[\w.@+-]+)/?$', views.results,),
                       (r'^fav/?$', views.fav,),
                       (r'^add/?$', views.add,),
                       (r'^remove/?$', views.remove,),

                       #(?P<username>[\w.@+-]+)/(?P<paper>[\w.@+-]+)/(?P<current>[\w.@+-]+)/(?P<q>[\w.@+-]+)/(?P<rate>[\w.@+-]+)/?$', views.fav,),
                       (r'^results_mod/$', views.results_mod),
                       (r'^authors/$', views.authors),
                       (r'^citations/$', views.citations),
                       (r'^references/$', views.references),

                       #url(r'^social-auth/', 'scholarec_web.app.views.social_auth'),
                       url(r'^login/?$', 'scholarec_web.app.views.login'),
                       url(r'^signup-email/', 'scholarec_web.app.views.signup_email'),
                       url(r'^email-sent/', 'scholarec_web.app.views.validation_sent'),
                       url(r'^logout/$', 'scholarec_web.app.views.logout'),
                       url(r'^done/$', 'scholarec_web.app.views.done', name='done'),
                       url(r'^email/$', 'scholarec_web.app.views.require_email', name='require_email'),
                       url(r'', include('social.apps.django_app.urls', namespace='social')),
                       
)

if settings.MODE == 'userena':
    urlpatterns += patterns('',
                            (r'^accounts/', include('userena.urls')),
                        )
elif settings.MODE == 'django_registration':
    urlpatterns += patterns('',
                            (r'^accounts/', include(
                                'registration.backends.default.urls')),
                        )
    
    
if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                            }),
    )
