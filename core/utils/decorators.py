"""
Custom decorators for SmartStock AI.
"""
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def staff_required(view_func):
    """
    Decorator to check if user is staff.
    """
    @wraps(view_func)
    @login_required
    def wrapper(request, *args, **kwargs):
        if not request.user.is_staff:
            return JsonResponse({'error': 'Staff access required'}, status=403)
        return view_func(request, *args, **kwargs)
    return wrapper


def ajax_required(view_func):
    """
    Decorator to check if request is AJAX.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'error': 'AJAX required'}, status=400)
        return view_func(request, *args, **kwargs)
    return wrapper
