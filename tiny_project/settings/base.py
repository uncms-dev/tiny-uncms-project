'''
Settings for your tiny CMS project.

For your reading pleasure, anything with a comment above it documents
settings that are specific to onespacemedia-cms. Everything else is left
uncommented on purpose. Thus, if you see a comment it is something you will
need to pay attention to, or at least copy-paste :)
'''

import os
import sys

# The CMS's page template functions assume this is present.
SITE_NAME = 'a tiny project'
# This too - it is used to turn relative /urls/ into http://actual.absolute/urls/.
SITE_DOMAIN = 'example.com'

# PublicationMiddleware will automagically exclude any objects that do not
# have their is_online field set from any querysets. Of course, you probably
# don't want to do that for EVERY request. Being able to view them in the
# admin is useful for administrators, after all :) You will want to change
# this if your admin lives anywhere but /admin/.
PUBLICATION_MIDDLEWARE_EXCLUDE_URLS = (
    '^admin/.*',
)

# This controls whether a new Page (and anything else that inherits from
# OnlineBase) will have `is_online` set to True by default. This is the
# default setting.
ONLINE_DEFAULT = True


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

    # Our basic CMS apps.
    'cms',
    # This gives you the Page class, the reason that we exist!
    'cms.apps.pages',
    # The media app is required by the Page class.
    'cms.apps.media',
    # This is not required at all, but it's handy. It provides a Link content
    # model that allows entries in your navigation to link to arbitrary URLs.
    'cms.apps.links',

    # Our local apps. You'll want to look at the code for them after you have
    # read this settings file.
    'tiny_project.apps.news',
    'tiny_project.apps.content',

    'django.contrib.admin',
]


# The CMS does not require this, but the TEMPLATES setting below does.
SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'DIRS': [
            os.path.join(SITE_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'match_extension': '.html',
            'match_regex': r'^(?!admin/|reversion/|registration/|jet.dashboard/|adminsortable2/|sitemap\.xml|debug_toolbar/).*',
            'app_dirname': 'templates',
            'newstyle_gettext': True,
            'autoescape': True,
            'auto_reload': False,
            'translation_engine': 'django.utils.translation',
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                # This puts the current page tree into the context, as `pages`.
                'cms.apps.pages.context_processors.pages',
                # Not at all necessary, but just about every project wants
                # access to `settings` (django.conf.settings) in their
                # template.
                'cms.context_processors.settings',
            ],
        },
    },
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
                'cms.context_processors.settings',
                'cms.apps.pages.context_processors.pages',
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
    # You will need both of these for onespacemedia-cms to function properly.
    # The first handles the CMS's publication system; it will ensure that
    # things with publication controls (pages, and anything else derived from
    # OnlineBase) do not show to logged-out users.
    'cms.middleware.PublicationMiddleware',
    # This annotates requests with the current page tree (as `request.pages`).
    'cms.apps.pages.middleware.PageMiddleware',
]

#
# TinyMCE options for the HTML editor (HtmlField).
# These map directly onto TinyMCE options. These are sensible defaults and are
# very close to what we use in production projects. More options are available
# here:
# https://www.tiny.cloud/docs-4x/configure/integration-and-setup/
#
WYSIWYG_OPTIONS = {
    # Overall height of the WYSIWYG
    'height': 500,

    # The one to pay attention to here is `cmsimage` - it allows you to insert
    # images from your media library.
    'plugins': [
        'advlist autolink link image lists charmap hr anchor pagebreak',
        'wordcount visualblocks visualchars code fullscreen cmsimage hr',
    ],
    # cmsimage here gives you the aforementioned item in your toolbar.
    'toolbar1': 'code | cut copy pastetext | undo redo | bullist numlist | link unlink anchor cmsimage | blockquote',
    'menubar': False,
    'toolbar_items_size': 'small',
    'block_formats': 'Paragraph=p;Header 2=h2;Header 3=h3;Header 4=h4;Header 5=h5;Header 6=h6;',
    'convert_urls': False,
    'paste_as_text': True,
    'image_advtab': True,
}

ALLOWED_HOSTS = [
    SITE_DOMAIN,
    'www.{}'.format(SITE_DOMAIN),
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
USE_L10N = True
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

if 'test' in sys.argv:
    # The CMS tests use test-only models, which won't be loaded if we only load
    # our real migration files, so point to a nonexistent one, which will make
    # the test runner fall back to 'syncdb' behavior.

    # Note: This will not catch a situation where a developer commits model
    # changes without the migration files.

    MIGRATION_MODULES = {}
    for app in INSTALLED_APPS:
        app_name = app.split('.')[-1]
        MIGRATION_MODULES[app_name] = None

    # Remove the localisation middleware
    if 'cms.middleware.LocalisationMiddleware' in MIDDLEWARE:
        MIDDLEWARE = tuple(
            c for c in MIDDLEWARE if c != 'cms.middleware.LocalisationMiddleware')
