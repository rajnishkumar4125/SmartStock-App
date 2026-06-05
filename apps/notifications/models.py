"""
Notification models.
"""
from django.db import models
from django.contrib.auth.models import User
from core.utils.constants import NOTIFICATION_TYPE_INFO, NOTIFICATION_TYPE_WARNING, NOTIFICATION_TYPE_ERROR, NOTIFICATION_TYPE_SUCCESS


class Notification(models.Model):
    """System notification model."""
    
    NOTIFICATION_TYPES = [
        (NOTIFICATION_TYPE_INFO, 'Info'),
        (NOTIFICATION_TYPE_WARNING, 'Warning'),
        (NOTIFICATION_TYPE_ERROR, 'Error'),
        (NOTIFICATION_TYPE_SUCCESS, 'Success'),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES,
        default=NOTIFICATION_TYPE_INFO
    )
    link = models.CharField(max_length=500, blank=True)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'read', '-created_at']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.title}"
    
    def mark_as_read(self):
        """Mark notification as read."""
        self.read = True
        self.save()
