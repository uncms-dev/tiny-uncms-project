import os
import sys


###
#  ___
# | _ ) __ _  ___ ___
# | _ \/ _` |(_-</ -_)
# |___/\__,_|/__/\___|
#
###
SITE_NAME = 'a tiny project'
SITE_DOMAIN = 'example.com'
PREPEND_WWW = True

# only required in this settings file
SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

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

# A secret key used for cryptographic algorithms. CHANGE THIS!!
# dd if=/dev/urandom of=/dev/stdout bs=50 count=1 | base64
SECRET_KEY = ''

# Ignores certain warnings on startup and/or `manage.py check`
SILENCED_SYSTEM_CHECKS = []

INSTALLED_APPS = [
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'sorl.thumbnail',

    'osm_jet',
    'cms',

    'reversion',
    'historylinks',
    'watson',

    'cms.apps.pages',
    'cms.apps.media',
    'cms.apps.links',

    'tiny_project.apps.news',
    'tiny_project.apps.content',

    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'adminsortable2',
]

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
            'bytecode_cache': {
                'name': 'default',
                'backend': 'django_jinja.cache.BytecodeCache',
                'enabled': False,
            },
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
                'cms.context_processors.settings',
                'cms.apps.pages.context_processors.pages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ]
        }
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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ]
        }
    }
]
# Namespace for cache keys, if using a process-shared cache.
CACHE_MIDDLEWARE_KEY_PREFIX = 'tiny_project'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

###
#  _                    _  _            _    _
# | |    ___  __  __ _ | |(_) ___ __ _ | |_ (_) ___  _ __
# | |__ / _ \/ _|/ _` || || |(_-</ _` ||  _|| |/ _ \| '  \
# |____|\___/\__|\__,_||_||_|/__/\__,_| \__||_|\___/|_||_|
#
###
# GEOIP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../geoip/'))
TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
USE_I18N = False
USE_L10N = True
USE_TZ = True


###
#  ___   _                  _        _
# |   \ (_) ___ _ __  __ _ | |_  __ | |__
# | |) || |(_-<| '_ \/ _` ||  _|/ _|| '  \
# |___/ |_|/__/| .__/\__,_| \__|\__||_||_|
#              |_|
###
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'watson.middleware.SearchContextMiddleware',
    'historylinks.middleware.HistoryLinkFallbackMiddleware',
    'cms.middleware.PublicationMiddleware',
    'cms.apps.pages.middleware.PageMiddleware',
]

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.Argon2PasswordHasher',
)
ROOT_URLCONF = 'tiny_project.urls'

WSGI_APPLICATION = 'tiny_project.wsgi.application'

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
SITE_ID = 1


###
#  _____  _     _          _                     _
# |_   _|| |_  (_) _ _  __| |   _ __  __ _  _ _ | |_  _  _
#   | |  | ' \ | || '_|/ _` |  | '_ \/ _` || '_||  _|| || |
#   |_|  |_||_||_||_|  \__,_|  | .__/\__,_||_|   \__| \_, |
#                              |_|                    |__/
###
PUBLICATION_MIDDLEWARE_EXCLUDE_URLS = (
    '^admin/.*',
)


JET_CHANGE_FORM_SIBLING_LINKS = False
JET_DEFAULT_THEME = 'osm'

ONLINE_DEFAULT = True

TINYPNG_API_KEY = ''

WYSIWYG_OPTIONS = {
    # Overall height of the WYSIWYG
    'height': 500,

    # Main plugins to load, this has been stripped to match the toolbar
    # See https://www.tinymce.com/docs/get-started/work-with-plugins/
    'plugins': [
        'advlist autolink link image lists charmap hr anchor pagebreak',
        'wordcount visualblocks visualchars code fullscreen cmsimage hr',
    ],

    # Items to display on the 3 toolbar lines
    'toolbar1': 'code | cut copy pastetext | undo redo | bullist numlist | link unlink anchor cmsimage | blockquote charmap',

    # Display menubar with dropdowns
    'menubar': False,

    # Make toolbar smaller
    'toolbar_items_size': 'small',

    'block_formats': 'Paragraph=p;Header 2=h2;Header 3=h3;Header 4=h4;Header 5=h5;Header 6=h6;',

    # Disable automatic URL manipulation
    'convert_urls': False,

    # Make TinyMCE past as text by default
    'paste_as_text': True,

    'image_advtab': True,
}


###
#  _   _        _                _          _     __      _          _    _
# | | | | _ __ | | ___  __ _  __| | ___  __| |   / /  ___| |_  __ _ | |_ (_) __
# | |_| || '_ \| |/ _ \/ _` |/ _` |/ -_)/ _` |  / /  (_-<|  _|/ _` ||  _|| |/ _|
#  \___/ | .__/|_|\___/\__,_|\__,_|\___|\__,_| /_/   /__/ \__|\__,_| \__||_|\__|
#        |_|
###
MEDIA_ROOT = '/var/www/tiny_project_media'
MEDIA_URL = '/media/'

STATIC_ROOT = '/var/www/tiny_project_static'
STATIC_URL = '/static/'

FILE_UPLOAD_PERMISSIONS = 0o644

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'assets'),  # For webpack_loader
    os.path.join(SITE_ROOT, 'static'),
)

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
    if 'cms.middleware.LocalisationMiddleware' in MIDDLEWARE_CLASSES:
        MIDDLEWARE_CLASSES = tuple(
            c for c in MIDDLEWARE_CLASSES if c != 'cms.middleware.LocalisationMiddleware')
