"""
Constants used throughout SmartStock AI.
"""

# Product statuses
PRODUCT_STATUS_ACTIVE = 'active'
PRODUCT_STATUS_INACTIVE = 'inactive'
PRODUCT_STATUS_DISCONTINUED = 'discontinued'

PRODUCT_STATUSES = [
    (PRODUCT_STATUS_ACTIVE, 'Active'),
    (PRODUCT_STATUS_INACTIVE, 'Inactive'),
    (PRODUCT_STATUS_DISCONTINUED, 'Discontinued'),
]

# Bill statuses
BILL_STATUS_DRAFT = 'draft'
BILL_STATUS_PAID = 'paid'
BILL_STATUS_PENDING = 'pending'
BILL_STATUS_CANCELLED = 'cancelled'

BILL_STATUSES = [
    (BILL_STATUS_DRAFT, 'Draft'),
    (BILL_STATUS_PAID, 'Paid'),
    (BILL_STATUS_PENDING, 'Pending'),
    (BILL_STATUS_CANCELLED, 'Cancelled'),
]

# Inventory transaction reasons
TRANSACTION_REASON_PURCHASE = 'purchase'
TRANSACTION_REASON_SALE = 'sale'
TRANSACTION_REASON_RETURN = 'return'
TRANSACTION_REASON_ADJUSTMENT = 'adjustment'

TRANSACTION_REASONS = [
    (TRANSACTION_REASON_PURCHASE, 'Purchase'),
    (TRANSACTION_REASON_SALE, 'Sale'),
    (TRANSACTION_REASON_RETURN, 'Return'),
    (TRANSACTION_REASON_ADJUSTMENT, 'Adjustment'),
]

# Pagination
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Cache timeouts (in seconds)
CACHE_TIMEOUT_SHORT = 300  # 5 minutes
CACHE_TIMEOUT_MEDIUM = 3600  # 1 hour
CACHE_TIMEOUT_LONG = 86400  # 1 day

# Notification types
NOTIFICATION_TYPE_INFO = 'info'
NOTIFICATION_TYPE_WARNING = 'warning'
NOTIFICATION_TYPE_ERROR = 'error'
NOTIFICATION_TYPE_SUCCESS = 'success'
