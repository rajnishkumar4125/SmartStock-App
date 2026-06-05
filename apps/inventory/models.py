"""
Inventory models for stock tracking.
"""
from django.db import models
from products.models import Product
from core.utils.constants import TRANSACTION_REASONS


class InventoryTransaction(models.Model):
    """Track all inventory transactions."""
    
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='transactions'
    )
    quantity_change = models.IntegerField(help_text="Positive or negative quantity")
    reason = models.CharField(
        max_length=20,
        choices=TRANSACTION_REASONS
    )
    reference_id = models.CharField(
        max_length=100,
        blank=True,
        help_text="Reference to bill or purchase order"
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['product', '-created_at']),
        ]
    
    def __str__(self):
        return f"{self.product.name} - {self.quantity_change} ({self.reason})"


class StockAudit(models.Model):
    """Periodic stock audit records."""
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='audits'
    )
    system_quantity = models.IntegerField()
    physical_quantity = models.IntegerField()
    difference = models.IntegerField()
    audited_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-audited_at']
    
    def __str__(self):
        return f"{self.product.name} - Audit {self.audited_at.date()}"


class ReorderLevel(models.Model):
    """Track reorder levels for products."""
    
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='reorder_config'
    )
    minimum_quantity = models.IntegerField()
    maximum_quantity = models.IntegerField()
    reorder_quantity = models.IntegerField()
    lead_time_days = models.IntegerField(default=7)
    
    def __str__(self):
        return f"{self.product.name} - Reorder: {self.reorder_quantity}"
