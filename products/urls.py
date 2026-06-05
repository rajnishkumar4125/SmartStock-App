from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete'),
    path('low-stock/', views.LowStockView.as_view(), name='low_stock'),
    path('bulk-upload/', views.BulkProductUploadView.as_view(), name='bulk_upload'),
    path('bulk-upload/results/', views.BulkProductUploadResultsView.as_view(), name='bulk_upload_results'),
    path('bulk-upload/download-sample/', views.DownloadProductSampleCSVView.as_view(), name='download_sample_csv'),
]
