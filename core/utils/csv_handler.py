"""
CSV Handler for bulk product and customer uploads.
Handles CSV parsing, validation, and data import.
"""
import csv
import io
from typing import List, Dict, Tuple, Any
from django.core.exceptions import ValidationError
from django.db import transaction
import pandas as pd


class CSVUploadResult:
    """Container for CSV upload results."""
    
    def __init__(self):
        self.successful = []
        self.failed = []
        self.total_processed = 0
        
    def add_success(self, row_num: int, data: Dict):
        """Add successful row."""
        self.successful.append({
            'row': row_num,
            'data': data
        })
        
    def add_failure(self, row_num: int, reason: str):
        """Add failed row with reason."""
        self.failed.append({
            'row': row_num,
            'reason': reason
        })
        
    def get_summary(self) -> Dict[str, Any]:
        """Get summary statistics."""
        return {
            'total_processed': len(self.successful) + len(self.failed),
            'successful': len(self.successful),
            'failed': len(self.failed),
            'success_rate': self._calculate_success_rate()
        }
    
    def _calculate_success_rate(self) -> float:
        """Calculate success rate percentage."""
        total = len(self.successful) + len(self.failed)
        if total == 0:
            return 0.0
        return round((len(self.successful) / total) * 100, 2)


class ProductCSVHandler:
    """Handler for product CSV uploads."""
    
    REQUIRED_FIELDS = ['name', 'sku', 'category', 'price', 'stock_quantity', 'reorder_level']
    OPTIONAL_FIELDS = ['description', 'status']
    
    @staticmethod
    def validate_and_import(csv_file) -> Tuple[CSVUploadResult, List[Dict]]:
        """
        Validate and import products from CSV file.
        
        Args:
            csv_file: InMemoryUploadedFile object
            
        Returns:
            Tuple of (CSVUploadResult, list of created products)
        """
        from products.models import Product, Category
        
        result = CSVUploadResult()
        created_products = []
        
        try:
            # Read CSV file
            stream = io.TextIOWrapper(csv_file.file, encoding='utf-8')
            reader = csv.DictReader(stream)
            
            if not reader.fieldnames:
                raise ValidationError("CSV file is empty or invalid format")
            
            # Verify required fields
            missing_fields = [f for f in ProductCSVHandler.REQUIRED_FIELDS 
                            if f not in reader.fieldnames]
            if missing_fields:
                raise ValidationError(f"Missing required fields: {', '.join(missing_fields)}")
            
            with transaction.atomic():
                for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is row 1)
                    try:
                        # Validate required fields
                        for field in ProductCSVHandler.REQUIRED_FIELDS:
                            if not row.get(field, '').strip():
                                raise ValueError(f"Missing required field: {field}")
                        
                        # Get or create category
                        category_name = row['category'].strip()
                        category, _ = Category.objects.get_or_create(
                            name=category_name,
                            defaults={'description': ''}
                        )
                        
                        # Prepare product data
                        product_data = {
                            'name': row['name'].strip(),
                            'sku': row['sku'].strip(),
                            'category': category,
                            'description': row.get('description', '').strip(),
                            'price': float(row['price']),
                            'stock_quantity': int(row['stock_quantity']),
                            'reorder_level': int(row['reorder_level']),
                            'status': row.get('status', 'active').strip().lower(),
                        }
                        
                        # Validate status
                        valid_statuses = ['active', 'inactive', 'discontinued']
                        if product_data['status'] not in valid_statuses:
                            raise ValueError(f"Invalid status: {product_data['status']}. "
                                           f"Must be one of {valid_statuses}")
                        
                        # Validate numeric fields
                        if product_data['price'] < 0:
                            raise ValueError("Price cannot be negative")
                        if product_data['stock_quantity'] < 0:
                            raise ValueError("Stock quantity cannot be negative")
                        if product_data['reorder_level'] < 0:
                            raise ValueError("Reorder level cannot be negative")
                        
                        # Check for duplicate SKU
                        if Product.objects.filter(sku=product_data['sku']).exists():
                            raise ValueError(f"SKU '{product_data['sku']}' already exists")
                        
                        # Create product
                        product = Product.objects.create(**product_data)
                        created_products.append(product)
                        result.add_success(row_num, {
                            'name': product.name,
                            'sku': product.sku
                        })
                        
                    except ValueError as e:
                        result.add_failure(row_num, str(e))
                    except Exception as e:
                        result.add_failure(row_num, f"Unexpected error: {str(e)}")
            
        except ValidationError as e:
            raise e
        except Exception as e:
            raise ValidationError(f"Error processing CSV file: {str(e)}")
        
        return result, created_products


class CustomerCSVHandler:
    """Handler for customer CSV uploads."""
    
    REQUIRED_FIELDS = ['name', 'email', 'phone', 'address', 'city', 'country']
    OPTIONAL_FIELDS = ['state', 'postal_code']
    
    @staticmethod
    def validate_and_import(csv_file) -> Tuple[CSVUploadResult, List[Dict]]:
        """
        Validate and import customers from CSV file.
        
        Args:
            csv_file: InMemoryUploadedFile object
            
        Returns:
            Tuple of (CSVUploadResult, list of created customers)
        """
        from customers.models import Customer
        from django.core.validators import validate_email
        
        result = CSVUploadResult()
        created_customers = []
        
        try:
            # Read CSV file
            stream = io.TextIOWrapper(csv_file.file, encoding='utf-8')
            reader = csv.DictReader(stream)
            
            if not reader.fieldnames:
                raise ValidationError("CSV file is empty or invalid format")
            
            # Verify required fields
            missing_fields = [f for f in CustomerCSVHandler.REQUIRED_FIELDS 
                            if f not in reader.fieldnames]
            if missing_fields:
                raise ValidationError(f"Missing required fields: {', '.join(missing_fields)}")
            
            with transaction.atomic():
                for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is row 1)
                    try:
                        # Validate required fields
                        for field in CustomerCSVHandler.REQUIRED_FIELDS:
                            if not row.get(field, '').strip():
                                raise ValueError(f"Missing required field: {field}")
                        
                        # Validate email
                        email = row['email'].strip()
                        try:
                            validate_email(email)
                        except ValidationError:
                            raise ValueError(f"Invalid email: {email}")
                        
                        # Check for duplicate email
                        if Customer.objects.filter(email=email).exists():
                            raise ValueError(f"Email '{email}' already exists")
                        
                        # Validate phone (basic validation: 10-15 digits)
                        phone = row['phone'].strip()
                        if not phone.isdigit() or not (10 <= len(phone) <= 15):
                            raise ValueError(f"Invalid phone: {phone} (must be 10-15 digits)")
                        
                        # Prepare customer data
                        customer_data = {
                            'name': row['name'].strip(),
                            'email': email,
                            'phone': phone,
                            'address': row['address'].strip(),
                            'city': row['city'].strip(),
                            'state': row.get('state', '').strip(),
                            'postal_code': row.get('postal_code', '').strip(),
                            'country': row['country'].strip(),
                        }
                        
                        # Create customer
                        customer = Customer.objects.create(**customer_data)
                        created_customers.append(customer)
                        result.add_success(row_num, {
                            'name': customer.name,
                            'email': customer.email
                        })
                        
                    except ValueError as e:
                        result.add_failure(row_num, str(e))
                    except Exception as e:
                        result.add_failure(row_num, f"Unexpected error: {str(e)}")
            
        except ValidationError as e:
            raise e
        except Exception as e:
            raise ValidationError(f"Error processing CSV file: {str(e)}")
        
        return result, created_customers


def generate_sample_csv(model_type: str) -> str:
    """Generate sample CSV template for bulk upload."""
    if model_type == 'products':
        headers = ProductCSVHandler.REQUIRED_FIELDS + ProductCSVHandler.OPTIONAL_FIELDS
        sample_data = [
            headers,
            ['Laptop', 'PROD-001', 'Electronics', '999.99', '50', '10', 'High-performance laptop', 'active'],
            ['Mouse', 'PROD-002', 'Electronics', '29.99', '200', '50', 'Wireless mouse', 'active'],
        ]
    elif model_type == 'customers':
        headers = CustomerCSVHandler.REQUIRED_FIELDS + CustomerCSVHandler.OPTIONAL_FIELDS
        sample_data = [
            headers,
            ['John Doe', 'john@example.com', '9876543210', '123 Main St', 'New York', 'NY', '10001', 'USA'],
            ['Jane Smith', 'jane@example.com', '9876543211', '456 Oak Ave', 'Los Angeles', 'CA', '90001', 'USA'],
        ]
    else:
        raise ValueError("Invalid model type")
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(sample_data)
    return output.getvalue()
