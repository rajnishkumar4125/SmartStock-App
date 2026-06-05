"""
Error handling middleware for SmartStock AI.
Handles exceptions and returns appropriate responses.
"""
import logging
import json
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class ErrorHandlingMiddleware(MiddlewareMixin):
    """
    Middleware to handle exceptions gracefully.
    """
    
    def process_exception(self, request, exception):
        # Log the exception
        logger.error(
            f"Exception in {request.method} {request.path}: {str(exception)}",
            exc_info=True
        )
        
        # Return JSON error response for API requests
        if request.path.startswith('/api/'):
            return JsonResponse(
                {
                    'error': 'Internal Server Error',
                    'message': str(exception) if logger.level == logging.DEBUG else 'An error occurred'
                },
                status=500
            )
        
        return None
