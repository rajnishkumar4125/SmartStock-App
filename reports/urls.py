from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('sales/', views.SalesReportView.as_view(), name='sales'),
]
