"""
Admin configuration for notifications app.
"""
from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'notification_type', 'read', 'created_at']
    list_filter = ['notification_type', 'read', 'created_at']
    search_fields = ['user__username', 'title', 'message']
    readonly_fields = ['created_at']
    
    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = 'Mark selected as read'
    
    actions = [mark_as_read]
