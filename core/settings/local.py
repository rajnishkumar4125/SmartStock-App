"""
Local settings for SmartStock AI project.
Used for local development with Docker.
"""
from .dev import *

# Override any development settings for Docker-based local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'smartstock_local'),
        'USER': os.getenv('DB_USER', 'smartstock'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'smartstock'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'ATOMIC_REQUESTS': True,
    }
}

# Use Redis for local development if available
try:
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://localhost:6379/0',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }
except Exception:
    pass  # Fall back to local memory cache if Redis is not available

print("✓ Local settings loaded")
