"""
Django settings for sysfolk project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _
from urllib.parse import urlparse

from decouple import config, Csv
from dj_database_url import parse as dburl
from django.contrib.messages import constants as message_constants

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

MESSAGE_LEVEL = message_constants.DEBUG

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

INTERNAL_IPS = ['127.0.0.1', '0.0.0.0']

ADMINS = [('Alessandro Folk', 'alessandrolimafolk@gmail.com'),]

# AUTH_USER_MODEL = 'core.User'
AUTH_USER_MODEL = 'authentication.MyUser'


# Email configuration

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

EMAIL_BACKEND = config('EMAIL_BACKEND')

EMAIL_HOST = config('EMAIL_HOST')

EMAIL_PORT = config('EMAIL_PORT', cast=int)

EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)

EMAIL_HOST_USER = config('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'test_without_migrations',
    'django_extensions',
    'debug_toolbar',

    'corsheaders',

    # 'rest_framework',
    # 'rest_framework.authtoken',
    # 'rest_auth',
    # # 'rest_framework_word_filter',

    'sysfolk.authentication.apps.AuthenticationConfig',
    'sysfolk.core.apps.CoreConfig',
    'sysfolk.financial.apps.FinancialConfig',
    'sysfolk.frontend',
]


# Cors Headers
CORS_ORIGIN_ALLOW_ALL = True


# Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # DjangoRestFramework
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'sysfolk.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'sysfolk.frontend.context_processors.context_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'sysfolk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-br'

# ugettext = lambda s: s
LANGUAGES = (
    ('pt-br', _('Brazilian Portuguese')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Django Jet
# http://jet.readthedocs.org/

JET_DEFAULT_THEME = 'default'  # default, green, light-violet, light-green, light-blue, light-gray

JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_SIDE_MENU_COMPACT = True

JET_SIDE_MENU_CUSTOM_APPS = [
    ('auth', ['__all__']),
    # ('auth', [
    #     'Group',
    # ]),
    ('authentication', ['__all__']),
    ('core', ['__all__']),
    ('financial', [
        # 'Category',
        # 'ClassificationCenter',
        # 'Bank',
        # 'DepositAccount',
        'AccountReceivable',
        'AccountPayable',
    ]),
]

JET_CHANGE_FORM_SIBLING_LINKS = True

JET_INDEX_DASHBOARD = 'sysfolk.dashboard.CustomIndexDashboard'

JET_APP_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultAppIndexDashboard'

# https://developers.google.com/analytics/devguides/config/mgmt/v3/quickstart/installed-py
JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, 'client_secrets.json')


# Frontend

SITE_NAME = 'SysFolk | Sistema financeiro online'
SITE_SHORT_NAME = 'SysFolk'

# Canonical SEO
SITE_CANONICAL = 'http://www.conttudoweb.com.br/'

# Social tags
SITE_KEYWORDS = 'sysfolk, sistema financeiro, sistemas financeiro online'
SITE_DESCRIPTION = 'Sistemas financeiro online.'
SITE_IMAGE = 'http://s3.amazonaws.com/creativetim_bucket/products/51/opt_mdp_thumbnail.jpg'  # TODO: Trocar esta imagem!

# Twitter Card data
TWITTER_SITE = '@conttudoweb'
TWITTER_CREATOR = '@sandrofolk'

# Open Graph data
SITE_FB_APP_ID = '6398915760047266458'
