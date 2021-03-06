# Django settings for challenge project.

# for dynamic settings
import os
PROJECT_DIR = os.path.dirname(__file__)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	 ('Mathias Boehn Grytemark', 'mathias@nuxis.org'),
)

MANAGERS = ADMINS


DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'challenge',
		'USER': 'challenge',
		'PASSWORD': 'challenge',
		'HOST': '127.0.0.1',
		'PORT': '',
	}
}

TIME_ZONE = 'Europe/Oslo'
LANGUAGE_CODE = 'en'

SITE_ID = 1

USE_I18N = True

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/amedia/'

SECRET_KEY = 't+q))2q)e6k6*ggeqw*bl9q3%_t-(e3#%!v$yl-l(s^rtabf!)'

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)
LOCALE_PATHS = (
	os.path.join(PROJECT_DIR, "locale/"), 
	)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
	 'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
	 'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'challenge.urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
	 'django.contrib.admin',
	 'django.contrib.staticfiles',
	 'challenge.levels',
	 'challenge.core',
	 'challenge.stats',
)

STATICFILES_DIRS = (
   os.path.join(PROJECT_DIR, "../static/"),
	)
TEMPLATE_DIRS = (
	 os.path.join(PROJECT_DIR, "templates"),
)
MEDIA_ROOT = os.path.join(PROJECT_DIR, "media/")

STATIC_ROOT = os.path.join(PROJECT_DIR, "static/")
STATIC_URL = '/static/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

try:
	from settings_local import *
except:
	pass

