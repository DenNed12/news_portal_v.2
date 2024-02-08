"""
Django settings for sitedir project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from os import path
from pathlib import Path
from dotenv import load_dotenv
import logging
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SITE_URL = 'http://127.0.0.1:8000'

DEFAULT_FROM_EMAIL = "deonissl@yandex.ru"

logger = logging.getLogger('django')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@@qq=v()c5h4_0x3e))eyc!nijwyj+8=2)03b8))d_n$4jma5u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'articles.apps.ArticlesConfig',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.locale.LocaleMiddleware',


]

ROOT_URLCONF = 'sitedir.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sitedir.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


LOGIN_REDIRECT_URL = "/news"


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
# registartion
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

#email


APSCEDULER_DATETIME_FORMAT = 'N J, Y, f:s a'
APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files')
    }}




LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'myformatter',
            'filters': ['require_debug_true']
        },
        'handle_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'myformatter1',
            'filters': ['require_debug_false']
        },
        'handle_warnings': {
            'level':'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'myformatter3'},

        'handle_erorrs': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter':'myformatter1',
            'filters': ['require_debug_false']},

        'handle_erorrs_mail': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'myformatter3',
            'filters': ['require_debug_false'],
            'include_html': True,
        },
        'handle_sequrity': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'sequrity.log',
            'formatter': 'myformatter1'}
    },

    'formatters': {
        'myformatter':{
            'format': '{asctime} {levelname} {message}',
            'datetime': '%Y.%m.%d',
            'style': '{',
        },
        'myformatter1': {
            'format': '{asctime} {levelname}  {module} {message}',
            'datetime': '%Y.%m.%d H%:M%:S%',
            'style': '{'
        },

        'myformatter2': {
            'format': '{asctime} {levelname} {pathname}  {message}',
            'datetime': '%Y.%m.%d H%:M%:S%',
            'style': '{'
        },

        'myformatter3': {
            'format': '{asctime} {levelname} {pathname} {exc_info} {message}',
            'datetime': '%Y.%m.%d H%:M%:S%',
            'style': '{'
        },

    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },

    },

    'loggers': {
        'django': {
            'handlers': ['console','handle_info','handle_warnings','handle_erorrs'],
            'level': 'DEBUG',
            'propagate': True,

        },
        'django.request': {
            'handlers': ['handle_erorrs','handle_erorrs_mail'],
            'propagate': True
        },
        'django.server': {
            'handlers': ['handle_erorrs','handle_erorrs_mail'],
            'propagate': True
        },
        'django.db.backends': {
            'handlers': ['handle_erorrs'],
            'propagate': True
        },

        'django.template': {
            'handlers': ['handle_erorrs'],
            'propagate': True,
        },

        'django.sequrity': {
            'handlers': ['handle_sequrity'],
            'propagate': True,
        }

    }

}


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]