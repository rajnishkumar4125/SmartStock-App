"""
Helper functions for SmartStock AI.
"""
from django.utils.text import slugify
from datetime import datetime, timedelta


def generate_bill_number():
    """
    Generate unique bill number.
    """
    from django.utils import timezone
    import uuid
    
    timestamp = timezone.now().strftime('%Y%m%d')
    unique_id = str(uuid.uuid4())[:8].upper()
    return f"BILL-{timestamp}-{unique_id}"


def format_currency(value):
    """
    Format value as currency.
    """
    return f"₹ {value:,.2f}"


def get_date_range(days=30):
    """
    Get date range for analytics.
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    return start_date, end_date


def slugify_string(string):
    """
    Convert string to slug.
    """
    return slugify(string)
