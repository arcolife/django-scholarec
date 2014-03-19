# Django settings for scholarec_web
import os
import sys

sys.path.insert(0, '../..')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db_scholarec',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Kolkata'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'static'),

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'sa7!a1cm3dc9vcmnty&amp;&amp;a=ibudkpk17r(^i5wk^y@u+v-fn&amp;9c'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'scholarec_web.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'scholarec_web.wsgi.application'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), \
                 'scholarec_web/templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'haystack',
    'search',
    'social.apps.django_app.default',
    'scholarec_web.app'
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

'''
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
'''

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
)

AUTHENTICATION_BACKENDS = (
    #'social.backends.amazon.AmazonOAuth2',
    #'social.backends.angel.AngelOAuth2',
    #'social.backends.aol.AOLOpenId',
    #'social.backends.appsfuel.AppsfuelOAuth2',
    #'social.backends.behance.BehanceOAuth2',
    #'social.backends.belgiumeid.BelgiumEIDOpenId',
    #'social.backends.bitbucket.BitbucketOAuth',
    #'social.backends.box.BoxOAuth2',
    #'social.backends.clef.ClefOAuth2',
    #'social.backends.coinbase.CoinbaseOAuth2',
    #'social.backends.dailymotion.DailymotionOAuth2',
    #'social.backends.disqus.DisqusOAuth2',
    #'social.backends.douban.DoubanOAuth2',
    #'social.backends.dropbox.DropboxOAuth',
    #'social.backends.evernote.EvernoteSandboxOAuth',
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.fedora.FedoraOpenId',
    #'social.backends.fitbit.FitbitOAuth',
    #'social.backends.flickr.FlickrOAuth',
    #'social.backends.foursquare.FoursquareOAuth2',
    'social.backends.github.GithubOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GooglePlusAuth',
    #'social.backends.instagram.InstagramOAuth2',
    #'social.backends.jawbone.JawboneOAuth2',
    'social.backends.linkedin.LinkedinOAuth',
    'social.backends.linkedin.LinkedinOAuth2',
    #'social.backends.live.LiveOAuth2',
    #'social.backends.livejournal.LiveJournalOpenId',
    #'social.backends.mailru.MailruOAuth2',
    #'social.backends.mendeley.MendeleyOAuth',
    #'social.backends.mendeley.MendeleyOAuth2',
    #'social.backends.mixcloud.MixcloudOAuth2',
    #'social.backends.odnoklassniki.OdnoklassnikiOAuth2',
    'social.backends.open_id.OpenIdAuth',
    #'social.backends.openstreetmap.OpenStreetMapOAuth',
    #'social.backends.orkut.OrkutOAuth',
    'social.backends.persona.PersonaAuth',
    #'social.backends.podio.PodioOAuth2',
    #'social.backends.rdio.RdioOAuth1',
    #'social.backends.rdio.RdioOAuth2',
    #'social.backends.readability.ReadabilityOAuth',
    'social.backends.reddit.RedditOAuth2',
    #'social.backends.runkeeper.RunKeeperOAuth2',
    #'social.backends.skyrock.SkyrockOAuth',
    'social.backends.soundcloud.SoundcloudOAuth2',
    'social.backends.stackoverflow.StackoverflowOAuth2',
    #'social.backends.steam.SteamOpenId',
    #'social.backends.stocktwits.StocktwitsOAuth2',
    #'social.backends.stripe.StripeOAuth2',
    #'social.backends.suse.OpenSUSEOpenId',
    #'social.backends.thisismyjam.ThisIsMyJamOAuth1',
    #'social.backends.trello.TrelloOAuth',
    #'social.backends.tripit.TripItOAuth',
    'social.backends.tumblr.TumblrOAuth',
    #'social.backends.twilio.TwilioAuth',
    'social.backends.twitter.TwitterOAuth',
    #'social.backends.vk.VKOAuth2',
    #'social.backends.weibo.WeiboOAuth2',
    #'social.backends.xing.XingOAuth',
    'social.backends.yahoo.YahooOAuth',
    #'social.backends.yahoo.YahooOpenId',
    #'social.backends.yammer.YammerOAuth2',
    #'social.backends.yandex.YandexOAuth2',
    #'social.backends.vimeo.VimeoOAuth1',
    'social.backends.email.EmailAuth',
    'social.backends.username.UsernameAuth',
    'django.contrib.auth.backends.ModelBackend',
)


'''
FACEBOOK_APP_ID              = ''
FACEBOOK_API_SECRET          = ''
LINKEDIN_CONSUMER_KEY        = ''
LINKEDIN_CONSUMER_SECRET     = ''
ORKUT_CONSUMER_KEY           = ''
ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
VK_APP_ID                    = ''
VK_API_SECRET                = ''
LIVE_CLIENT_ID               = ''
LIVE_CLIENT_SECRET           = ''
SKYROCK_CONSUMER_KEY         = ''
SKYROCK_CONSUMER_SECRET      = ''
YAHOO_CONSUMER_KEY           = ''
YAHOO_CONSUMER_SECRET        = ''
READABILITY_CONSUMER_SECRET  = ''
READABILITY_CONSUMER_SECRET  = ''
'''

# SOCIAL_AUTH_FACEBOOK_APP_ID = ''
# SOCIAL_AUTH_FACEBOOK_SECRET = ''
# SOCIAL_AUTH_FACEBOOK_APP_NAMESPACE = ''
# SOCIAL_AUTH_FACEBOOK_EXTENDED_PERMISSIONS = ['email']

SOCIAL_AUTH_TWITTER_KEY         = ''
SOCIAL_AUTH_TWITTER_SECRET      = ''
SOCIAL_AUTH_GITHUB_KEY          = ''
SOCIAL_AUTH_GITHUB_SECRET       = ''

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/done/'
URL_PATH = ''
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

SOCIAL_AUTH_EMAIL_FORM_URL = '/signup-email'
SOCIAL_AUTH_EMAIL_FORM_HTML = 'email_signup.html'
SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'scholarec_web.app.mail.send_validation'
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/email-sent/'
# SOCIAL_AUTH_USERNAME_FORM_URL = '/signup-username'                       
SOCIAL_AUTH_USERNAME_FORM_HTML = 'username_signup.html'

SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/userinfo.profile'
]

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'scholarec_web.app.pipeline.require_email',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


