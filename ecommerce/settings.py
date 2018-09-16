"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url
from decouple import config




# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config("SECRET_KEY", None)




# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

DEBUG = True
ALLOWED_HOSTS = []
BASE_URL ="www.sylimarket.com"






# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Third party
    'storages',


    #Local*
    'accounts',
    'addresses',
    'analytics',
    'billing',
    'carts',
    'orders',
    'marketing',
    'products',
    'search',
    'tags',

]

AUTH_USER_MODEL ="accounts.User" #changes the built-in user model to ours M

DEFAULT_ACTIVATION_DAYS = 7


FORCE_SESSION_TO_ONE = False
FORCE_INACTIVE_USER_END_SESSION = False

MAILCHIMP_API_KEY = config("MAILCHIMP_API_KEY", None)
MAILCHIMP_DATA_CENTER = config("MAILCHIMP_DATA_CENTER", None)
MALCHIMP_EMAIL_LIST_ID = config("MALCHIMP_EMAIL_LIST_ID", None)





STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY", None)

STRIPE_PUB_KEY = config("STRIPE_PUB_KEY", None)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',


]

ROOT_URLCONF = 'ecommerce.urls'


LOGOUT_REDIRECT_URL = "accounts:login"

LOGIN_URL = 'accounts:login'
LOGOUT_URL = 'accounts:logout'
LOGIN_REDIRECT_URL = 'home'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.i18n",
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'



DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2'
    }
}



# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# SECURE_PROXY_SSL_HEADER = ("HTT_X_FORWARED_PROTO", "https")



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = "Africa/Casablanca"


USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
PROTECTED_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "protected_root")




EMAIL_HOST = config("EMAIL_HOST", None)
EMAIL_HOST_USER =config("EMAIL_HOST_USER", None)
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", None)
EMAIL_PORT = "587"
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", None)


ADMINS = [ 

        ("Excellence Michel","bnvnmmnl@gmail.com"),
]


MANAGERS = ADMINS


from .production import *

if os.environ.get("ENV") =="PRODUCTION":
    from ecommerce.aws.conf import *




