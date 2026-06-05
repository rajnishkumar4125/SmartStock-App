from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import models
from .forms import UserRegistrationForm
from products.models import Product
from customers.models import Customer
from billing.models import Bill

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('accounts:login')
        return render(request, 'accounts/register.html', {'form': form})

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'
    login_url = 'accounts:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get counts for dashboard statistics
        context['total_products'] = Product.objects.count()
        context['total_customers'] = Customer.objects.count()
        context['pending_bills'] = Bill.objects.filter(status='pending').count()
        context['low_stock_items'] = Product.objects.filter(
            stock_quantity__lte=models.F('reorder_level')
        ).count()
        
        # Get recent activities
        context['recent_products'] = Product.objects.all().order_by('-created_at')[:5]
        context['recent_customers'] = Customer.objects.all().order_by('-created_at')[:5]
        
        return context
