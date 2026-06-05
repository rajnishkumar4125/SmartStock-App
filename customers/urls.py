from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='list'),
    path('create/', views.CustomerCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.CustomerUpdateView.as_view(), name='update'),
    path('bulk-upload/', views.BulkCustomerUploadView.as_view(), name='bulk_upload'),
    path('bulk-upload/results/', views.BulkCustomerUploadResultsView.as_view(), name='bulk_upload_results'),
    path('bulk-upload/download-sample/', views.DownloadCustomerSampleCSVView.as_view(), name='download_sample_csv'),
]
