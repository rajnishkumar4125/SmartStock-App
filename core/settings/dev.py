"""
Development settings for SmartStock AI project.
"""
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Database - SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email Configuration for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Cache for development - use simple local memory cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'smartstock-dev-cache',
    }
}

# Logging - verbose for development
LOGGING['loggers']['django']['level'] = 'DEBUG'

# Development toolbar - disabled for now due to URL resolution issues
if DEBUG:
    MIDDLEWARE.remove('django.middleware.security.SecurityMiddleware')
    # Debug toolbar disabled - uncomment when URLs are fully configured
    # INSTALLED_APPS += ['debug_toolbar']
    # MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    # INTERNAL_IPS = ['127.0.0.1']

print("[OK] Development settings loaded")
