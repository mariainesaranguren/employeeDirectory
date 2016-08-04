"""
Django settings for mysite project.
Generated by 'django-admin startproject' using Django 1.9.8.
For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from djangae.settings_base import *

# Running manage.py sets the DJANGO_SETTINGS_MODULE environment variable,
# which gives Django the Python import path to your mysite/settings.py file.

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

#TODO: Keep SECRET_KEY secret and turn DEBUG off.

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's-9pww!gu)0p4*u70gf3q@wq4h3$ac=6ul*w+&rkc*szultnjf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Project variables
project_id = 'wizeline-employee-directory'
gae_db_instance = 'wz-employee-directory'
db_name = 'employee_directory'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',     # With this Django automatically looks for an admin module in each application and imports it. It is the admin site. You will use it shortly.
    'employee_directory',
    'django_filters',
    'django_tables2',
    'django.contrib.auth',      # Django admin dependency, an authentication system.
    'django.contrib.contenttypes',  # Django admin dependency, a framework for content types.
    'django.contrib.sessions',  # Django admin dependency, a session framework.
    'django.contrib.messages',  # Django admin dependency, a messaging framework.
    'django.contrib.staticfiles',   # Django admin dependency, a framework for managing static files.
    'djangae',
]

MIDDLEWARE_CLASSES = [ # For django use.
    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  #Added for django admin
    'django.contrib.messages.middleware.MessageMiddleware',     #Added for django admin
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'mysite/templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request', #Added for django-tables2 app
                'django.contrib.auth.context_processors.auth', #Added for django admin
                'django.contrib.messages.context_processors.messages', #Added for django admin
            ],
        },
        # 'LOADERS': 'django.template.loaders.filesystem.Loader',
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'
APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT', '')

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
import pdb; pdb.set_trace()
if APP_ENVIRONMENT in ['development']:
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
       # Running on production App Engine, so use a Google Cloud SQL database.
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.mysql',
               'HOST': '/cloudsql/%s:%s' % (project_id, gae_db_instance),
               'NAME': db_name,
               'USER': 'root',
           }
       }
    else:
         # Running on production App Engine, so use a Google Cloud SQL database.
         DATABASES = {
             'default': {
                 'ENGINE': 'django.db.backends.mysql',
                 'HOST': os.getenv('DB_HOST', ''),
                 'NAME': db_name,
                 'USER': 'migrater',    # TODO Analyze this
                 'PASSWORD': os.getenv('DB_PASSWORD', '')
             }
         }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': db_name,
            'USER': 'root',
            'HOST': '127.0.0.1',
        }
    }

DEFAULT_INDEX_TABLESPACE = 'employees'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT= os.path.join(BASE_DIR, 'static') # The directory from which you would like to serve these files
STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     '/var/www/static/',
# ]


# Media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #'/Users/mariainesaranguren/Wizeline/mysite'
MEDIA_URL = '/media/' #'http://localhost:8000/'
#TODO: Change MEDIA_ROOT and MEDIA_URL
