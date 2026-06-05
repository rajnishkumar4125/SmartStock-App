from django.db import models
from django.core.validators import EmailValidator, RegexValidator

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\d{10,15}$')])
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name
    
    
