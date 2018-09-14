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

SECRET_KEY = """4g[5VAJ}v9~`=Zxn}B}{!DE.xT(M1YNpGTq   V"Q1    EaHf_EQbM;A>jcj%}|ayrgr;"=:?O9H?"""




# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

DEBUG = True
ALLOWED_HOSTS = []






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





STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY")

STRIPE_PUB_KEY = config("STRIPE_PUB_KEY")


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


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': config("DB_NAME"),
'USER': config("DB_USER"),
'PASSWORD': config("DB_PASSWORD"),
'HOST': config("DB_HOST"),
'PORT': '',
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


STATICFILES_DIRS = [
         os.path.join(BASE_DIR, "static_my_proj"),
                
                ]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "static_root")

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media_root")
PROTECTED_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "protected_root")




EMAIL_HOST = config("EMAIL_HOST", None)
EMAIL_HOST_USER =config("EMAIL_HOST_USER", None)
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", None)
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool)

DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", None)


ADMINS = [ 

        ("Excellence Michel","bnvnmmnl@gmail.com"),
]


MANAGERS = ADMINS


CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_HSTS_SECONDS             = None
SECURE_FRAME_DENY               = False






