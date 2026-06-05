"""
Serializers for SmartStock AI REST API v1.
"""
from rest_framework import serializers
from apps.products.models import Product, Category
from apps.customers.models import Customer
from apps.billing.models import Bill, BillItem


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'category', 'category_name', 'description', 
                  'price', 'stock_quantity', 'reorder_level', 'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer model."""
    
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'address', 'city', 'state', 
                  'postal_code', 'country', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class BillItemSerializer(serializers.ModelSerializer):
    """Serializer for BillItem model."""
    product_name = serializers.CharField(source='product.name', read_only=True)
    total = serializers.SerializerMethodField()
    
    class Meta:
        model = BillItem
        fields = ['id', 'bill', 'product', 'product_name', 'quantity', 'price', 'total']
    
    def get_total(self, obj):
        return obj.get_total()


class BillSerializer(serializers.ModelSerializer):
    """Serializer for Bill model."""
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    items = BillItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Bill
        fields = ['id', 'bill_number', 'customer', 'customer_name', 'total_amount', 
                  'status', 'notes', 'items', 'created_at', 'updated_at']
        read_only_fields = ['bill_number', 'created_at', 'updated_at']
