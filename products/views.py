from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm, BulkProductUploadForm
from core.utils.csv_handler import ProductCSVHandler, generate_sample_csv
from django.db import models

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 20

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:list')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:list')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('products:list')

class LowStockView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/low_stock.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(stock_quantity__lte=models.F('reorder_level'))

class BulkProductUploadView(LoginRequiredMixin, FormView):
    """View for bulk product CSV upload."""
    template_name = 'products/bulk_upload.html'
    form_class = BulkProductUploadForm
    success_url = reverse_lazy('products:bulk_upload_results')
    
    def form_valid(self, form):
        csv_file = form.cleaned_data['csv_file']
        
        try:
            result, created_products = ProductCSVHandler.validate_and_import(csv_file)
            
            # Store results in session
            self.request.session['upload_results'] = {
                'type': 'products',
                'summary': result.get_summary(),
                'successful': result.successful,
                'failed': result.failed,
                'total_created': len(created_products)
            }
            
            # Add success message
            summary = result.get_summary()
            messages.success(
                self.request,
                f"Upload completed! {summary['successful']} products imported successfully."
            )
            
            if summary['failed'] > 0:
                messages.warning(
                    self.request,
                    f"{summary['failed']} products failed to import. Review details below."
                )
            
            return redirect('products:bulk_upload_results')
            
        except ValidationError as e:
            messages.error(self.request, f"CSV validation error: {str(e)}")
            return self.form_invalid(form)
        except Exception as e:
            messages.error(self.request, f"Upload failed: {str(e)}")
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        """Handle invalid form submission."""
        return self.render_to_response(self.get_context_data(form=form))

class BulkProductUploadResultsView(LoginRequiredMixin, ListView):
    """View to display bulk product upload results."""
    template_name = 'products/bulk_upload_results.html'
    context_object_name = 'results'
    
    def get_queryset(self):
        # Return empty queryset, we'll use session data instead
        return []
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        upload_results = self.request.session.get('upload_results', {})
        context['upload_results'] = upload_results
        context['type'] = 'Products'
        return context

class DownloadProductSampleCSVView(LoginRequiredMixin, View):
    """Download sample CSV template for products."""
    
    def get(self, request):
        csv_content = generate_sample_csv('products')
        response = HttpResponse(csv_content, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products_sample.csv"'
        return response


