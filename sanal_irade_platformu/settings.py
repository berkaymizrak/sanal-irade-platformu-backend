"""
Django settings for sanal_irade_platformu project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import django_smtp_ssl
import environ
from pathlib import Path
import os

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS', cast=list)

# Must be defined for Django 4+
CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS', cast=list)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'tools.apps.ToolsConfig',
    'user.apps.UserConfig',
    'election.apps.ElectionConfig',
    'contact.apps.ContactConfig',
    'mailqueue',
    'django_celery_beat',
    'parler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Language middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sanal_irade_platformu.urls'

AUTH_USER_MODEL = 'user.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # Extra
            ],
        },
    },
]

WSGI_APPLICATION = 'sanal_irade_platformu.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'tr-TR'

LANGUAGES = [
    ('tr', 'Turkish'),
    ('en', 'English'),
]

PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE

LANGUAGE_CODES = tuple({'code': LANGUAGE[0]} for LANGUAGE in LANGUAGES)

PARLER_LANGUAGES = {
    None: LANGUAGE_CODES,
    'default': {
        'fallbacks': [LANGUAGE_CODE],  # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,  # the default; let .active_translations() return fallbacks too.
    },
}

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings

vars().update(env.email_url())
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_BACKEND = env('EMAIL_BACKEND')

# Celery settings
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://redis_resume:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis_resume:6379/0')

CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Istanbul'
CELERY_ENABLE_UTC = False  # DEFAULT True
CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 * 2  # Seconds (2 days)
BROKER_POOL_LIMIT = 1
BROKER_HEARTBEAT = None
USER_AGENTS_CACHE = None

# Mail Queue settings
# pip install django-mail-queue

# If you're using Celery, set this to True
MAILQUEUE_CELERY = True  # DEFAULT False

# Enable the mail queue. If this is set to False, the mail queue will be disabled and emails will be
# sent immediately instead.
MAILQUEUE_QUEUE_UP = True

# Maximum amount of emails to send during each queue run
MAILQUEUE_LIMIT = 1
