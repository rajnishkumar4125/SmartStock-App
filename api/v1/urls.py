"""
REST API v1 for SmartStock AI.
"""
from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()

# Product endpoints
router.register(r'products', viewsets.ProductViewSet, basename='product')
router.register(r'categories', viewsets.CategoryViewSet, basename='category')

# Customer endpoints
router.register(r'customers', viewsets.CustomerViewSet, basename='customer')

# Billing endpoints
router.register(r'bills', viewsets.BillViewSet, basename='bill')
router.register(r'bill-items', viewsets.BillItemViewSet, basename='bill-item')

# Reports endpoints
router.register(r'reports', viewsets.ReportsViewSet, basename='reports')

urlpatterns = router.urls
