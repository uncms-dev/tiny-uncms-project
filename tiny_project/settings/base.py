"""
Settings for your tiny UnCMS project.

For your reading pleasure, anything with a comment above it documents
settings that are specific to UnCMS. Everything else is left uncommented on
purpose. Thus, if you see a comment it is something you will need to pay
attention to, or at least copy-paste :)
"""

import os

SITE_NAME = 'a tiny project'

# This isn't used by UnCMS (it expects this in its configuration dict), but
# let's define it here rather than several times in this file.
SITE_DOMAIN = 'example.com'

UNCMS = {
    # The only required setting! This will be used to canonicalise URLs, from
    # /paths/ to https://actual.urls/paths/
    'SITE_DOMAIN': SITE_DOMAIN,
    # This controls whether a new Page (and anything else that inherits from
    # OnlineBase) will have `is_online` set to True by default. Let's override
    # the default setting for the funs (and as an example).
    'ONLINE_DEFAULT': False,
}


DATA_UPLOAD_MAX_MEMORY_SIZE = 20621440

INSTALLED_APPS = [
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    # This is required for the thumbnailing in the Media app's admin.
    'sorl.thumbnail',

    'reversion',
    'watson',

    # Our basic UnCMS apps.
    'uncms',
    # This gives you the Page class, the reason that we exist!
    'uncms.pages',
    # The media app is required by the Page class.
    'uncms.media',
    # This is not required at all, but it's handy. It provides a Link content
    # model that allows entries in your navigation to link to arbitrary URLs.
    'uncms.links',
    # This is also totally optional, but almost every site (especially sites
    # which already existed before being converted to UnCMS) will require
    # something like it. This allows creating redirects from one URL to
    # another. It will be under "Redirects" in your admin.
    'uncms.redirects',

    # Our local apps. You'll want to look at the code for them after you have
    # read this settings file.
    'tiny_project.apps.news',
    'tiny_project.apps.content',

    'django.contrib.admin',
]


# UnCMS does not require this, but the TEMPLATES setting below does.
SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'uncms.pages.context_processors.pages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'watson.middleware.SearchContextMiddleware',
    # You will need both of these for UnCMS to function properly. The first
    # handles UnCMS's publication system; it will ensure that things with
    # publication controls (pages, and anything else derived from OnlineBase)
    # do not show to logged-out users.
    'uncms.middleware.PublicationMiddleware',
    # This annotates requests with the current page tree (as `request.pages`).
    'uncms.pages.middleware.PageMiddleware',
    # This handles redirects from broken URLs to new ones.
    'uncms.redirects.middleware.RedirectFallbackMiddleware',
]

ALLOWED_HOSTS = [
    SITE_DOMAIN,
    f'www.{SITE_DOMAIN}',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
    }
}

SECRET_KEY = ''

SILENCED_SYSTEM_CHECKS = []

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
USE_I18N = False
USE_TZ = True

ROOT_URLCONF = 'tiny_project.urls'

WSGI_APPLICATION = 'tiny_project.wsgi.application'

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
SITE_ID = 1

FILE_UPLOAD_PERMISSIONS = 0o644

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
)

STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
