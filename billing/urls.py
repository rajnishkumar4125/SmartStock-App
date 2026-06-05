from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('', views.BillListView.as_view(), name='list'),
    path('create/', views.BillCreateView.as_view(), name='create'),
    path('<int:pk>/invoice/', views.BillInvoicePDFView.as_view(), name='invoice'),
    path('<int:pk>/edit/', views.BillUpdateView.as_view(), name='update'),
    path('<int:pk>/', views.BillDetailView.as_view(), name='detail'),
]
