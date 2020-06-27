"""
Django settings for synchro project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import environ

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
ROOT_DIR = (
    environ.Path(__file__) - 3
)  # (synchronl/synchro/synchro/settings/base.py - 3 = synchronl/)

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env(str(ROOT_DIR.path('.env')))

print(str(ROOT_DIR.path('.env')))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

ALLOWED_HOSTS = [
    "cbssilhouettes.nlartisticswimming.com",
    "*.cbssilhouettes.nlartisticswimming.com",
    "summitsynchro.synchronl.com",
    "synchronl.com",
    "www.synchronl.com",
    "www.nlartisticswimming.com",
    ".nlartisticswimming.com",
    "*.nlartisticswimming.com",
    "summitsynchro.nlartisticswimming.com",
    "127.0.0.1",
]


# False if not in os.environ
#DEBUG = env('DEBUG')
DEBUG = True

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')


SUMMIT_API_KEY = env('STRIPE_SUMMIT')
SYNCHRONL_API_KEY = env('STRIPE_NLARTS')


# Application definition
INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Wagtail requirements
    "taggit",
    "compressor",
    "modelcluster",
    # Wagtail admin override
    "dashboard",
    # Wagtail itself
    "wagtail.core",
    "wagtail.admin",
    "wagtail.search",
    "wagtail.images",
    "wagtail.documents",
    "wagtail.snippets",
    "wagtail.users",
    "wagtail.sites",
    "wagtail.embeds",
    "wagtail.contrib.redirects",
    "wagtail.contrib.forms",
    "wagtail.contrib.search_promotions",
    # Other 3rd party apps
    #    'twitter_tag',
    # Default wagtail apps
    "search",
    "home",
    # In-house apps
    "common",
    "blog",
    "person",
    "about",
    "sponsor",
    "gallery",
    "gdrive",
    "event",
    "document",
    "team",
    "form",
    "payment",
)

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.core.middleware.SiteMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
)

ROOT_URLCONF = "synchro.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "builtins": [],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION = "synchro.wsgi.application"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

STATICFILES_DIRS = (os.path.join(PROJECT_DIR, "static"),)

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Wagtail settings

WAGTAIL_SITE_NAME = "Synchro"
WAGTAILADMIN_RECENT_EDITS_LIMIT = 5
WAGTAIL_ENABLE_UPDATE_CHECK = False
TAGGIT_CASE_INSENSITIVE = True


# Twitter settings
# Your access token: Access token
TWITTER_OAUTH_TOKEN = ""
# Your access token: Access token secret
TWITTER_OAUTH_SECRET = ""
# OAuth settings: Consumer key
TWITTER_CONSUMER_KEY = ""
# OAuth settings: Consumer secret
TWITTER_CONSUMER_SECRET = ""


# Hacky? TODO
try:
    from .local import *
except ImportError:
    pass