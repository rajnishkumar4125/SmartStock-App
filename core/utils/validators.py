"""
Validators for SmartStock AI.
"""
from django.core.exceptions import ValidationError
import re


def validate_phone_number(value):
    """
    Validate phone number format.
    """
    pattern = r'^\d{10,15}$'
    if not re.match(pattern, value):
        raise ValidationError('Phone number must be 10-15 digits')


def validate_gst_number(value):
    """
    Validate GST number format (Indian GST).
    """
    pattern = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$'
    if not re.match(pattern, value):
        raise ValidationError('Invalid GST number format')


def validate_sku(value):
    """
    Validate SKU format.
    """
    if len(value) < 3 or len(value) > 20:
        raise ValidationError('SKU must be between 3 and 20 characters')


def validate_positive_number(value):
    """
    Validate that number is positive.
    """
    if value <= 0:
        raise ValidationError('Number must be positive')
