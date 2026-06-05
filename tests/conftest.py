"""
Pytest configuration for SmartStock AI.
"""
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_system.settings')
django.setup()

pytest_plugins = ['pytest_django']
