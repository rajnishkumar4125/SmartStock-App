"""
Analytics models.
"""
from django.db import models


class SalesAnalytics(models.Model):
    """Store aggregated sales analytics."""
    
    date = models.DateField(unique=True)
    total_revenue = models.DecimalField(max_digits=12, decimal_places=2)
    total_bills = models.IntegerField()
    average_bill_value = models.DecimalField(max_digits=10, decimal_places=2)
    top_product_name = models.CharField(max_length=200)
    total_units_sold = models.IntegerField()
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Sales Analytics'


class InventoryAnalytics(models.Model):
    """Store inventory analytics."""
    
    date = models.DateField(unique=True)
    total_products = models.IntegerField()
    low_stock_count = models.IntegerField()
    out_of_stock_count = models.IntegerField()
    total_inventory_value = models.DecimalField(max_digits=15, decimal_places=2)
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Inventory Analytics'


class CustomerAnalytics(models.Model):
    """Store customer analytics."""
    
    date = models.DateField(unique=True)
    new_customers = models.IntegerField()
    total_customers = models.IntegerField()
    repeat_customers = models.IntegerField()
    customer_retention_rate = models.FloatField()
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Customer Analytics'
