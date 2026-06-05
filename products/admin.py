from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'category', 'price', 'stock_quantity', 'reorder_level', 'status']
    list_filter = ['category', 'status', 'created_at']
    search_fields = ['name', 'sku']
    readonly_fields = ['created_at', 'updated_at']
