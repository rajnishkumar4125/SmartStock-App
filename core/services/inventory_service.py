"""
Inventory service for SmartStock AI.
Handles inventory tracking and management.
"""
from django.db import transaction


class InventoryService:
    """
    Service class for inventory operations.
    """
    
    @staticmethod
    @transaction.atomic
    def update_stock(product, quantity_change, reason):
        """
        Update product stock with transaction tracking.
        """
        from apps.inventory.models import InventoryTransaction
        from apps.products.models import Product
        
        product.stock_quantity += quantity_change
        product.save()
        
        # Log the transaction
        InventoryTransaction.objects.create(
            product=product,
            quantity_change=quantity_change,
            reason=reason
        )
        
        return product
    
    @staticmethod
    def get_low_stock_products():
        """
        Get all products with low stock.
        """
        from apps.products.models import Product
        
        return Product.objects.filter(
            stock_quantity__lte=models.F('reorder_level'),
            status='active'
        )
    
    @staticmethod
    def check_stock_availability(product, quantity):
        """
        Check if product has sufficient stock.
        """
        return product.stock_quantity >= quantity
