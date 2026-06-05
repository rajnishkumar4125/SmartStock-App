"""
ViewSets for SmartStock AI REST API v1.
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.products.models import Product, Category
from apps.customers.models import Customer
from apps.billing.models import Bill, BillItem
from .serializers import (
    CategorySerializer, ProductSerializer, CustomerSerializer,
    BillSerializer, BillItemSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for Category model."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for Product model."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['name', 'sku', 'category__name']
    ordering_fields = ['name', 'price', 'stock_quantity', 'created_at']
    filterset_fields = ['category', 'status']
    
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        """Get products with low stock."""
        low_stock_products = self.queryset.filter(
            stock_quantity__lte=models.F('reorder_level')
        )
        serializer = self.get_serializer(low_stock_products, many=True)
        return Response(serializer.data)


class CustomerViewSet(viewsets.ModelViewSet):
    """ViewSet for Customer model."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['name', 'email', 'phone']
    ordering_fields = ['name', 'created_at']


class BillItemViewSet(viewsets.ModelViewSet):
    """ViewSet for BillItem model."""
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer
    permission_classes = [IsAuthenticated]


class BillViewSet(viewsets.ModelViewSet):
    """ViewSet for Bill model."""
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['bill_number', 'customer__name']
    ordering_fields = ['bill_number', 'total_amount', 'created_at']
    filterset_fields = ['status', 'customer']
    
    @action(detail=True, methods=['post'])
    def mark_paid(self, request, pk=None):
        """Mark bill as paid."""
        bill = self.get_object()
        bill.status = 'paid'
        bill.save()
        return Response({'status': 'Bill marked as paid'})
    
    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get all pending bills."""
        pending_bills = self.queryset.filter(status='pending')
        serializer = self.get_serializer(pending_bills, many=True)
        return Response(serializer.data)


class ReportsViewSet(viewsets.ViewSet):
    """ViewSet for reports and analytics."""
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def sales_summary(self, request):
        """Get sales summary."""
        from django.db.models import Sum, Count
        
        total_sales = Bill.objects.filter(status='paid').aggregate(
            total=Sum('total_amount')
        )
        total_bills = Bill.objects.count()
        pending_bills = Bill.objects.filter(status='pending').count()
        
        return Response({
            'total_sales': total_sales['total'] or 0,
            'total_bills': total_bills,
            'pending_bills': pending_bills,
        })
    
    @action(detail=False, methods=['get'])
    def inventory_summary(self, request):
        """Get inventory summary."""
        from django.db.models import Sum, Count, Q
        
        total_products = Product.objects.count()
        low_stock = Product.objects.filter(
            Q(stock_quantity__lte=models.F('reorder_level')) & 
            Q(status='active')
        ).count()
        
        return Response({
            'total_products': total_products,
            'low_stock_products': low_stock,
        })
