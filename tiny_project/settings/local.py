import os
import os.path

from .base import *  # pylint: disable=unused-wildcard-import,wildcard-import

# Run in debug mode.

DEBUG = True

TEMPLATES[0]['OPTIONS']['auto_reload'] = DEBUG

MEDIA_ROOT = os.path.expanduser(os.path.join('~/Sites', SITE_DOMAIN, 'media'))
STATIC_ROOT = os.path.expanduser(os.path.join('~/Sites', SITE_DOMAIN, 'static'))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

SITE_DOMAIN = 'localhost:8000'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

PREPEND_WWW = False
