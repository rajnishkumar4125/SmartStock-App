from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm, BulkCustomerUploadForm
from core.utils.csv_handler import CustomerCSVHandler, generate_sample_csv

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 20

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customers:list')

class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'

class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customers:list')

class BulkCustomerUploadView(LoginRequiredMixin, FormView):
    """View for bulk customer CSV upload."""
    template_name = 'customers/bulk_upload.html'
    form_class = BulkCustomerUploadForm
    success_url = reverse_lazy('customers:bulk_upload_results')
    
    def form_valid(self, form):
        csv_file = form.cleaned_data['csv_file']
        
        try:
            result, created_customers = CustomerCSVHandler.validate_and_import(csv_file)
            
            # Store results in session
            self.request.session['upload_results'] = {
                'type': 'customers',
                'summary': result.get_summary(),
                'successful': result.successful,
                'failed': result.failed,
                'total_created': len(created_customers)
            }
            
            # Add success message
            summary = result.get_summary()
            messages.success(
                self.request,
                f"Upload completed! {summary['successful']} customers imported successfully."
            )
            
            if summary['failed'] > 0:
                messages.warning(
                    self.request,
                    f"{summary['failed']} customers failed to import. Review details below."
                )
            
            return redirect('customers:bulk_upload_results')
            
        except ValidationError as e:
            messages.error(self.request, f"CSV validation error: {str(e)}")
            return self.form_invalid(form)
        except Exception as e:
            messages.error(self.request, f"Upload failed: {str(e)}")
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        """Handle invalid form submission."""
        return self.render_to_response(self.get_context_data(form=form))

class BulkCustomerUploadResultsView(LoginRequiredMixin, ListView):
    """View to display bulk customer upload results."""
    template_name = 'customers/bulk_upload_results.html'
    context_object_name = 'results'
    
    def get_queryset(self):
        # Return empty queryset, we'll use session data instead
        return []
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        upload_results = self.request.session.get('upload_results', {})
        context['upload_results'] = upload_results
        context['type'] = 'Customers'
        return context

class DownloadCustomerSampleCSVView(LoginRequiredMixin, View):
    """Download sample CSV template for customers."""
    
    def get(self, request):
        csv_content = generate_sample_csv('customers')
        response = HttpResponse(csv_content, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="customers_sample.csv"'
        return response


