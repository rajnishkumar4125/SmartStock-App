"""
Billing service for SmartStock AI.
Handles all billing-related business logic.
"""
from decimal import Decimal
from django.db import transaction


class BillingService:
    """
    Service class for billing operations.
    """
    
    @staticmethod
    @transaction.atomic
    def create_bill(customer, items_data):
        """
        Create a new bill with items.
        """
        from apps.billing.models import Bill, BillItem
        
        bill = Bill.objects.create(customer=customer)
        
        total_amount = Decimal('0.00')
        for item_data in items_data:
            bill_item = BillItem.objects.create(
                bill=bill,
                product=item_data['product'],
                quantity=item_data['quantity'],
                price=item_data['price']
            )
            total_amount += bill_item.get_total()
        
        bill.total_amount = total_amount
        bill.save()
        
        return bill
    
    @staticmethod
    def calculate_bill_total(bill):
        """
        Calculate and update bill total.
        """
        total = sum(item.get_total() for item in bill.items.all())
        bill.total_amount = total
        bill.save()
        return total
    
    @staticmethod
    def apply_discount(bill, discount_percent):
        """
        Apply discount to bill.
        """
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError('Discount percentage must be between 0 and 100')
        
        discount_amount = bill.total_amount * Decimal(discount_percent) / Decimal(100)
        bill.total_amount -= discount_amount
        bill.save()
        
        return bill.total_amount
