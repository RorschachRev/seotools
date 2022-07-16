"""
Django settings for seotools project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3qc_%ft78ljlo7qxkk-%dg#l2g@&)pr$aym^#c4k^3gx%a3#k('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS=( '/home/seo/dev-tools/tools/templates', )

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.sites',
    'tools',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tools.urls'

WSGI_APPLICATION = 'tools.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#DATABASE_ROUTERS = ['manager.router.DatabaseAppsRouter']
#DATABASE_ROUTERS = ['django.db.utils.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {'wn':'wn', 'wp':'wp'}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'wn':{
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'wn_sg',
        'USER': 'wn_sg',
        'PASSWORD': 'JNf8Aa87yhU7273U',
        'HOST': 'localhost',
        'PORT': '',
    },
    'wp':{
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'sg_wp',
        'USER': 'sg_wp',
        'PASSWORD': 'K4zaWcpQ8Yw6KK59',
        'HOST': 'localhost',
        'PORT': '',
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
LOGGING = {
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handers': ['console'],
        },
    },
    'version': 1,
}
