import io
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Bill
from .forms import BillForm, BillItemFormSet
from products.models import Product

class BillListView(LoginRequiredMixin, ListView):
    model = Bill
    template_name = 'billing/bill_list.html'
    context_object_name = 'bills'
    paginate_by = 20

class BillCreateView(LoginRequiredMixin, View):
    template_name = 'billing/create_bill.html'
    login_url = 'accounts:login'

    def get(self, request, *args, **kwargs):
        form = BillForm()
        formset = BillItemFormSet(prefix='items')
        return render(request, self.template_name, {
            'form': form,
            'formset': formset,
            'product_prices_json': json.dumps(self.get_product_prices()),
        })

    def post(self, request, *args, **kwargs):
        form = BillForm(request.POST)
        formset = BillItemFormSet(request.POST, prefix='items')
        if form.is_valid() and formset.is_valid():
            bill = form.save(commit=False)
            bill.status = 'pending'
            bill.save()
            formset.instance = bill
            formset.save()
            bill.calculate_total()
            return redirect('billing:detail', pk=bill.pk)

        return render(request, self.template_name, {
            'form': form,
            'formset': formset,
            'product_prices': self.get_product_prices(),
        })

    def get_product_prices(self):
        return {str(product.id): str(product.price) for product in Product.objects.filter(status='active')}

class BillDetailView(LoginRequiredMixin, DetailView):
    model = Bill
    template_name = 'billing/bill_detail.html'
    context_object_name = 'bill'

class BillUpdateView(LoginRequiredMixin, View):
    template_name = 'billing/create_bill.html'
    login_url = 'accounts:login'

    def get(self, request, pk, *args, **kwargs):
        bill = get_object_or_404(Bill, pk=pk)
        form = BillForm(instance=bill)
        formset = BillItemFormSet(instance=bill, prefix='items')
        return render(request, self.template_name, {
            'form': form,
            'formset': formset,
            'product_prices_json': json.dumps(self.get_product_prices()),
            'bill': bill,
        })

    def post(self, request, pk, *args, **kwargs):
        bill = get_object_or_404(Bill, pk=pk)
        form = BillForm(request.POST, instance=bill)
        formset = BillItemFormSet(request.POST, instance=bill, prefix='items')
        if form.is_valid() and formset.is_valid():
            bill = form.save()
            formset.save()
            bill.calculate_total()
            return redirect('billing:detail', pk=bill.pk)

        return render(request, self.template_name, {
            'form': form,
            'formset': formset,
            'product_prices_json': json.dumps(self.get_product_prices()),
            'bill': bill,
        })

    def get_product_prices(self):
        return {str(product.id): str(product.price) for product in Product.objects.filter(status='active')}

class BillInvoicePDFView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        bill = get_object_or_404(Bill, pk=pk)
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter)
        pdf.setTitle(f"Invoice - {bill.bill_number}")
        pdf.setFont('Helvetica-Bold', 18)
        pdf.drawString(50, 760, 'Invoice')

        pdf.setFont('Helvetica', 10)
        pdf.drawString(50, 735, f'Bill Number: {bill.bill_number}')
        pdf.drawString(50, 720, f'Date: {bill.created_at.strftime("%Y-%m-%d")}')
        pdf.drawString(50, 705, f'Customer: {bill.customer.name}')
        pdf.drawString(50, 690, f'Email: {bill.customer.email}')
        pdf.drawString(50, 675, f'Phone: {bill.customer.phone}')

        pdf.drawString(50, 650, 'Items:')
        pdf.setFont('Helvetica-Bold', 10)
        pdf.drawString(50, 635, 'Product')
        pdf.drawString(280, 635, 'Qty')
        pdf.drawString(350, 635, 'Price')
        pdf.drawString(430, 635, 'Total')

        y_position = 620
        pdf.setFont('Helvetica', 10)
        for item in bill.items.all():
            if y_position < 100:
                pdf.showPage()
                y_position = 750
            pdf.drawString(50, y_position, item.product.name)
            pdf.drawString(280, y_position, str(item.quantity))
            pdf.drawString(350, y_position, f"{item.price:.2f}")
            pdf.drawString(430, y_position, f"{item.get_total():.2f}")
            y_position -= 18

        y_position -= 12
        pdf.setFont('Helvetica-Bold', 12)
        pdf.drawString(350, y_position, 'Grand Total:')
        pdf.drawString(430, y_position, f"{bill.total_amount:.2f}")

        pdf.showPage()
        pdf.save()
        buffer.seek(0)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{bill.bill_number}.pdf"'
        response.write(buffer.getvalue())
        return response
