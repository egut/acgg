# -*- coding: utf-8 -*-
# Django settings for acgg project.
import os

#This will load development settings. 
DEBUG = True
TEMPLATE_DEBUG = DEBUG



#Remove .../acgg/settings.py
PROJECT_ROOT = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ADMINS = (
    (u'Erik Günther', 'erik.gunther@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'acgg',
        'USER': 'acgg_user',
        'PASSWORD': 'acgg_passwd',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Make this unique, and don't share it with anybody.
SECRET_KEY = '+767li!rcai+g6-^6863e9z#vue833*hdaj%&*f#gmqd6kz*9-'



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Stockholm'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'sv'


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
MEDIA_URL = "/media/"


STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, "acgg", "static"),
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    # allauth templates: you could copy this directory into your
    # project and tweak it according to your needs
    # os.path.join(PROJECT_ROOT, 'templates', 'uniform', 'allauth'),
    # example project specific templates
    os.path.join(PROJECT_ROOT, 'templates') , 
)

TEMPLATE_CONTEXT_PROCESSORS = (    
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'acgg.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'acgg.wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#########################################################################
# ADMIN

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)

#########################################################################
# AVATAR

INSTALLED_APPS += (
    'avatar', )



#########################################################################
# ALLAUTH

AUTHENTICATION_BACKENDS += (
    "allauth.account.auth_backends.AuthenticationBackend",
)


TEMPLATE_CONTEXT_PROCESSORS += (
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

INSTALLED_APPS += (
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
#    'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
#    'allauth.socialaccount.providers.github',
#    'allauth.socialaccount.providers.linkedin',
#    'allauth.socialaccount.providers.openid',
#    'allauth.socialaccount.providers.persona',
#    'allauth.socialaccount.providers.soundcloud',
#    'allauth.socialaccount.providers.stackexchange',
#    'allauth.socialaccount.providers.twitch',
#    'allauth.socialaccount.providers.twitter',
#    'allauth.socialaccount.providers.vimeo',
#    'allauth.socialaccount.providers.weibo',
)


# django-allauth Configuration variables you might like to change.
#

# Specifies the login method to use -- whether the user logs in by entering
# his username, e-mail address, or either one of both. Possible values
# are 'username' | 'email' | 'username_email'
# ACCOUNT_AUTHENTICATION_METHOD

# The URL to redirect to after a successful e-mail confirmation, in case no
# user is logged in. Default value is settings.LOGIN_URL.
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL

# The URL to redirect to after a successful e-mail confirmation, in case of
# an authenticated user. Default is settings.LOGIN_REDIRECT_URL
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL

# Determines the expiration date of email confirmation mails (# of days).
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

# The user is required to hand over an e-mail address when signing up.
ACCOUNT_EMAIL_REQUIRED = True

# Determines the e-mail verification method during signup. When set to
# "mandatory" the user is blocked from logging in until the email
# address is verified. Choose "optional" or "none" to allow logins
# with an unverified e-mail address. In case of "optional", the e-mail
# verification mail is still sent, whereas in case of "none" no e-mail
# verification mails are sent.
# ACCOUNT_EMAIL_VERIFICATION = "optional"

# Subject-line prefix to use for email messages sent. By default, the name
# of the current Site (django.contrib.sites) is used.
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Acgg] '

# A string pointing to a custom form class (e.g. 'myapp.forms.SignupForm')
# that is used during signup to ask the user for additional input
# (e.g. newsletter signup, birth date). This class should implement a
# 'save' method, accepting the newly signed up user as its only parameter.
# ACCOUNT_SIGNUP_FORM_CLASS = None

# When signing up, let the user type in his password twice to avoid typ-o's.
# ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True

# Enforce uniqueness of e-mail addresses.
ACCOUNT_UNIQUE_EMAIL = False

# A callable (or string of the form 'some.module.callable_name') that takes
# a user as its only argument and returns the display name of the user. The
# default implementation returns user.username.
# ACCOUNT_USER_DISPLAY

# An integer specifying the minimum allowed length of a username.
# ACCOUNT_USERNAME_MIN_LENGTH = 1

# The user is required to enter a username when signing up. Note that the
# user will be asked to do so even if ACCOUNT_AUTHENTICATION_METHOD is set
# to email. Set to False when you do not wish to prompt the user to enter a
# username.
# ACCOUNT_USERNAME_REQUIRED = True

# render_value parameter as passed to PasswordInput fields.
# ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False

# An integer specifying the minimum password length.
# ACCOUNT_PASSWORD_MIN_LENGTH = 6

# Request e-mail address from 3rd party account provider? E.g. using OpenID
# AX, or the Facebook 'email' permission.
#SOCIALACCOUNT_QUERY_EMAIL = True

# Attempt to bypass the signup form by using fields (e.g. username, email)
# retrieved from the social account provider. If a conflict arises due to a
# duplicate e-mail address the signup form will still kick in.
# SOCIALACCOUNT_AUTO_SIGNUP = True

# Enable support for django-avatar. When enabled, the profile image of the
# user is copied locally into django-avatar at signup. Default is
# 'avatar' in settings.INSTALLED_APPS.
SOCIALACCOUNT_AVATAR_SUPPORT = True

# Dictionary containing provider specific settings.
# SOCIALACCOUNT_PROVIDERS
SOCIALACCOUNT_PROVIDERS = \
    { 'google':
        { 'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile'],
          'AUTH_PARAMS': { 'access_type': 'online' } }}



#########################################################################
# DEVELOPMENT

if DEBUG:
    # Hosts/domain names that are valid for this site; required if DEBUG is False
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ['127.0.0.1']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(PROJECT_ROOT, 'acgg.db'),
        }
    }

