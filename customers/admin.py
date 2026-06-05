from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'city', 'created_at']
    list_filter = ['created_at', 'city']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['created_at', 'updated_at']
