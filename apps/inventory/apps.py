"""
Inventory app for SmartStock AI.
Handles inventory tracking and stock management.
"""
from django.apps import AppConfig


class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.inventory'
    verbose_name = 'Inventory Management'
