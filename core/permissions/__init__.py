"""
Custom permissions for SmartStock AI REST API.
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner
        return obj.owner == request.user


class IsStaff(permissions.BasePermission):
    """
    Permission to check if user is staff member.
    """
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsAuthenticated(permissions.BasePermission):
    """
    Permission to check if user is authenticated.
    """
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
