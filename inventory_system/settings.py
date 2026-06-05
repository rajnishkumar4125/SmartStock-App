"""
Configure SmartStock AI settings module.
This file allows Django to find the correct settings file based on environment.
"""
import os
from pathlib import Path

# Determine which settings to use based on environment
ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev').lower()

if ENVIRONMENT == 'prod':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.prod')
elif ENVIRONMENT == 'local':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.dev')

# Import the appropriate settings module
if ENVIRONMENT == 'prod':
    from core.settings.prod import *
elif ENVIRONMENT == 'local':
    from core.settings.local import *
else:
    from core.settings.dev import *
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
