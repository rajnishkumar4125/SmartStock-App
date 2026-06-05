"""
Notification service for SmartStock AI.
Handles email and in-app notifications.
"""
from django.core.mail import send_mail
from django.conf import settings


class NotificationService:
    """
    Service class for sending notifications.
    """
    
    @staticmethod
    def send_low_stock_alert(product):
        """
        Send low stock alert email to staff.
        """
        subject = f'Low Stock Alert: {product.name}'
        message = f'Product {product.name} (SKU: {product.sku}) has low stock. Current stock: {product.stock_quantity}'
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=True,
        )
    
    @staticmethod
    def send_bill_notification(bill, recipient_email):
        """
        Send bill notification email.
        """
        subject = f'Invoice {bill.bill_number}'
        message = f'Your bill {bill.bill_number} has been created. Total: {bill.total_amount}'
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            fail_silently=True,
        )
    
    @staticmethod
    def send_registration_confirmation(user):
        """
        Send registration confirmation email.
        """
        subject = 'Welcome to SmartStock AI'
        message = f'Welcome {user.first_name}! Your account has been created successfully.'
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=True,
        )
