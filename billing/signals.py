from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BillItem

@receiver(post_save, sender=BillItem)
def update_bill_total_on_item_save(sender, instance, created, **kwargs):
    instance.bill.calculate_total()

@receiver(post_delete, sender=BillItem)
def update_bill_total_on_item_delete(sender, instance, **kwargs):
    instance.bill.calculate_total()
