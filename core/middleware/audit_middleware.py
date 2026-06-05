"""
Audit middleware for SmartStock AI.
Logs user actions and API calls for audit trail.
"""
import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class AuditMiddleware(MiddlewareMixin):
    """
    Middleware to log all user actions for audit purposes.
    """
    
    def process_request(self, request):
        # Store request start time for duration tracking
        import time
        request._start_time = time.time()
        return None
    
    def process_response(self, request, response):
        # Log API requests
        if request.path.startswith('/api/'):
            duration = getattr(request, '_start_time', 0)
            if duration:
                duration = time.time() - duration
            
            logger.info(
                f"API Request: {request.method} {request.path} "
                f"Status: {response.status_code} Duration: {duration:.2f}s"
            )
        
        return response
