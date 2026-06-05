"""
Admin configuration for analytics app.
"""
from django.contrib import admin
from .models import SalesAnalytics, InventoryAnalytics, CustomerAnalytics


@admin.register(SalesAnalytics)
class SalesAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['date', 'total_revenue', 'total_bills', 'average_bill_value']
    list_filter = ['date']
    date_hierarchy = 'date'
    readonly_fields = ['date']


@admin.register(InventoryAnalytics)
class InventoryAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['date', 'total_products', 'low_stock_count', 'out_of_stock_count']
    list_filter = ['date']
    date_hierarchy = 'date'
    readonly_fields = ['date']


@admin.register(CustomerAnalytics)
class CustomerAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['date', 'new_customers', 'total_customers', 'customer_retention_rate']
    list_filter = ['date']
    date_hierarchy = 'date'
    readonly_fields = ['date']
