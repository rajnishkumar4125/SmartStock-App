"""
Admin configuration for inventory app.
"""
from django.contrib import admin
from .models import InventoryTransaction, StockAudit, ReorderLevel


@admin.register(InventoryTransaction)
class InventoryTransactionAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity_change', 'reason', 'created_at']
    list_filter = ['reason', 'created_at']
    search_fields = ['product__name', 'reference_id']
    readonly_fields = ['created_at']


@admin.register(StockAudit)
class StockAuditAdmin(admin.ModelAdmin):
    list_display = ['product', 'system_quantity', 'physical_quantity', 'difference', 'audited_at']
    list_filter = ['audited_at']
    search_fields = ['product__name']
    readonly_fields = ['audited_at']


@admin.register(ReorderLevel)
class ReorderLevelAdmin(admin.ModelAdmin):
    list_display = ['product', 'minimum_quantity', 'maximum_quantity', 'reorder_quantity']
    search_fields = ['product__name']
