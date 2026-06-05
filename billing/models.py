from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from customers.models import Customer
from products.models import Product
import uuid

class Bill(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    ]

    bill_number = models.CharField(max_length=50, unique=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='bills')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.bill_number:
            self.bill_number = f"BILL-{timezone.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.bill_number

    def calculate_total(self):
        self.total_amount = sum(item.get_total() for item in self.items.all())
        self.save()

class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.bill.bill_number} - {self.product.name}"

# Signals to auto-update bill total
@receiver(post_save, sender=BillItem)
def update_bill_on_item_save(sender, instance, **kwargs):
    instance.bill.calculate_total()

@receiver(post_delete, sender=BillItem)
def update_bill_on_item_delete(sender, instance, **kwargs):
    instance.bill.calculate_total()
