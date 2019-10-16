import os
import os.path

from .base import *  # pylint: disable=unused-wildcard-import,wildcard-import

# Run in debug mode.

DEBUG = True

TEMPLATES[0]['OPTIONS']['auto_reload'] = DEBUG

# Save media files to the user's Sites folder.

MEDIA_ROOT = os.path.expanduser(os.path.join('~/Sites', SITE_DOMAIN, 'media'))
STATIC_ROOT = os.path.expanduser(os.path.join('~/Sites', SITE_DOMAIN, 'static'))

# Never used in production! Do not use this in production.
SECRET_KEY = 'inTUqgV6migfo0WbssBg+zhK5VI9RWDm7NExfBraPGbdwS30xILlwYn+9Ry4x+Pv3ao'


# Use local server.

SITE_DOMAIN = 'localhost:8000'

ALLOWED_HOSTS = [
    # Django's defaults.
    '127.0.0.1',
    'localhost',
]

PREPEND_WWW = False

# Optional separate database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
    },
}

CACHES['default']['BACKEND'] = 'django.core.cache.backends.dummy.DummyCache'
