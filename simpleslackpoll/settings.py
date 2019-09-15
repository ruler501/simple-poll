"""
Django settings for simpleslackpoll project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("POLLS_SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG

ALLOWED_HOSTS = os.environ.get("POLLS_HOST", "localhost;127.0.0.1").split(';')

# Application definition

INSTALLED_APPS = (
    'main',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'simpleslackpoll.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'simpleslackpoll.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

REMOTE_DATABASE = os.environ.get("POLLS_DATABASE_URL", None)
POLLS_DATABASE = os.environ.get("POLLS_DATABASE", "local").lower()
if POLLS_DATABASE != "local" and POLLS_DATABASE != "dj" and REMOTE_DATABASE is not None:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POLLS_DATABASE_NAME", None),
        'USER': os.environ.get("POLLS_DATABASE_USERNAME", None),
        'PASSWORD': os.environ.get("POLLS_DATABASE_PASSWORD", None),
        'HOST': REMOTE_DATABASE,
        'PORT': os.environ.get("POLLS_DATABASE_PORT", None)
    }
else:
    # Parse database configuration from $DATABASE_URL
    config = dj_database_url.config()
    if config and POLLS_DATABASE != "local":
        DATABASES['default'] = config
