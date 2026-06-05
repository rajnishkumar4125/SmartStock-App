from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Count
from billing.models import Bill, BillItem
from products.models import Product

class SalesReportView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/sales_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Sales statistics
        context['total_sales'] = Bill.objects.filter(status='paid').aggregate(Sum('total_amount'))['total_amount__sum'] or 0
        context['total_orders'] = Bill.objects.count()
        context['top_products'] = BillItem.objects.values('product__name').annotate(total=Sum('quantity')).order_by('-total')[:10]
        
        return context
