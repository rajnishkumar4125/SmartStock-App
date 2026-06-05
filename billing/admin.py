from django.contrib import admin
from .models import Bill, BillItem

class BillItemInline(admin.TabularInline):
    model = BillItem
    extra = 1

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['bill_number', 'customer', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['bill_number', 'customer__name']
    readonly_fields = ['bill_number', 'created_at', 'updated_at']
    inlines = [BillItemInline]
