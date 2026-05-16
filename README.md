# SmartStock AI - Intelligent Inventory & Billing Management System

SmartStock AI is a modern Django-based inventory and billing management system designed for learning advanced full-stack development and scalable software architecture.

The project focuses on:

- **Inventory Management**: Comprehensive product and stock tracking
- **Billing & Invoice Generation**: Professional invoice creation with GST support
- **Customer Management**: Complete customer database and relationship tracking
- **REST API Development**: DRF-based APIs for future integrations
- **React Frontend Integration**: Modern UI with real-time updates
- **AI-Powered Forecasting**: Intelligent stock predictions and sales forecasting
- **Docker-Based Local Development**: Containerized local environment for consistency

The application is currently optimized for local development using Docker Desktop while maintaining a scalable architecture for future production deployment.

---

## Project Vision

The goal of SmartStock AI is to build a modern inventory ecosystem for small and medium businesses with intelligent automation and scalable architecture.

This project is being developed as:

- **Professional Portfolio Project**: Demonstrate advanced Django and full-stack capabilities
- **Advanced Django Learning Project**: Explore advanced patterns, architecture, and best practices
- **Full-Stack Engineering Practice**: Complete development lifecycle from requirements to deployment
- **Future SaaS-Ready Application**: Architected for multi-tenancy and production scaling

---

## Core Features

### Inventory Management
- Product CRUD operations with full validation
- SKU management and uniqueness enforcement
- Category management and hierarchical organization
- Real-time inventory tracking
- Low stock alerts and automatic notifications
- Inventory transaction history and audit logs
- Product status management (active/inactive/discontinued)
- Batch operations and bulk updates

### Billing System
- Professional invoice generation
- GST-ready billing calculations
- Automatic total and tax calculations
- PDF invoice support and export
- Bill history tracking with status updates
- Bill numbering system with auto-generation
- Payment tracking and reconciliation
- Multiple payment methods support

### Customer Management
- Comprehensive customer profiles
- Complete contact details and addresses
- Purchase history and transaction tracking
- Customer segmentation and analytics
- Contact preferences and communication history
- Customer lifecycle management

### Authentication & Security
- Custom user model (future implementation)
- Role-based access control (RBAC)
- JWT authentication for APIs
- Secure login system with 2FA (planned)
- Session management
- Audit logging and security events

### Dashboard & Analytics
- Revenue tracking and trends
- Sales reports with period comparison
- Top-selling products analytics
- Inventory insights and stock analysis
- Interactive charts and visualizations
- KPI dashboards
- Customizable reports

### AI Features (Planned)
- Sales forecasting using time-series analysis
- Smart stock prediction algorithms
- Reorder recommendations based on patterns
- Demand forecasting
- Price optimization suggestions

---

## Technology Stack

### Backend
- **Python 3.13+**: Core programming language
- **Django 6.0.5**: Web framework
- **Django REST Framework**: RESTful API development
- **Celery**: Asynchronous task queue (planned)
- **Redis**: Caching and task broker (planned)

### Frontend
- **React.js 18+**: Interactive UI framework (planned)
- **Tailwind CSS**: Utility-first CSS framework
- **Bootstrap 5**: Responsive design (current)
- **Chart.js / ApexCharts**: Data visualization
- **Axios**: HTTP client for API calls (planned)

### Database
- **PostgreSQL 14+**: Primary production database
- **SQLite3**: Development and testing database

### Async & Caching
- **Redis**: In-memory data store for caching
- **Celery**: Distributed task processing
- **RabbitMQ**: Message broker (optional)

### Local Development & Deployment
- **Docker**: Container platform
- **Docker Compose**: Multi-container orchestration
- **Docker Desktop**: Local development environment

### AI & Analytics
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms
- **Matplotlib / Plotly**: Data visualization libraries

### Testing & Quality
- **pytest**: Testing framework
- **pytest-django**: Django testing utilities
- **coverage.py**: Code coverage measurement
- **Black**: Code formatter
- **Flake8**: Code linter
- **isort**: Import sorter

---

## Project Architecture

```text
smartstock-ai/

├── apps/                           # Django applications
│   ├── accounts/                   # User authentication & management
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── templates/
│   │
│   ├── products/                   # Product & category management
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── admin.py
│   │   ├── urls.py
│   │   └── templates/
│   │
│   ├── inventory/                  # Stock tracking & management
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   └── templates/
│   │
│   ├── billing/                    # Billing & invoice system
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── signals.py
│   │   ├── admin.py
│   │   ├── urls.py
│   │   └── templates/
│   │
│   ├── customers/                  # Customer management
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── admin.py
│   │   ├── urls.py
│   │   └── templates/
│   │
│   ├── reports/                    # Sales reports & analytics
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── templates/
│   │
│   ├── analytics/                  # Advanced analytics (planned)
│   │   ├── models.py
│   │   ├── services.py
│   │   └── views.py
│   │
│   └── notifications/              # Notification system (planned)
│       ├── models.py
│       ├── services.py
│       └── tasks.py
│
├── api/                            # REST API endpoints
│   ├── v1/
│   │   ├── serializers.py
│   │   ├── viewsets.py
│   │   └── urls.py
│   │
│   └── v2/ (planned)
│
├── frontend/                       # React frontend (planned)
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
│
├── core/                           # Core project configuration
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py                # Base settings
│   │   ├── dev.py                 # Development settings
│   │   ├── prod.py                # Production settings
│   │   └── local.py               # Local environment settings
│   │
│   ├── services/                  # Business logic services
│   │   ├── billing_service.py
│   │   ├── inventory_service.py
│   │   ├── notification_service.py
│   │   └── export_service.py
│   │
│   ├── middleware/                # Custom middleware
│   │   ├── audit_middleware.py
│   │   └── error_handling.py
│   │
│   ├── permissions/               # DRF permissions
│   │   ├── base.py
│   │   └── custom_permissions.py
│   │
│   ├── utils/                     # Utility functions
│   │   ├── decorators.py
│   │   ├── helpers.py
│   │   ├── validators.py
│   │   └── constants.py
│   │
│   ├── urls.py                    # Main URL configuration
│   ├── wsgi.py                    # WSGI configuration
│   └── asgi.py                    # ASGI configuration
│
├── docker/                        # Docker configurations
│   ├── Dockerfile
│   ├── Dockerfile.prod
│   └── entrypoint.sh
│
├── templates/                     # Django templates
│   ├── base.html
│   ├── accounts/
│   ├── products/
│   ├── customers/
│   ├── billing/
│   ├── reports/
│   └── includes/
│
├── static/                        # Static files
│   ├── css/
│   ├── js/
│   ├── images/
│   └── vendor/
│
├── media/                         # User-uploaded files
│   ├── products/
│   ├── invoices/
│   └── documents/
│
├── requirements/                  # Dependency files
│   ├── base.txt                   # Base requirements
│   ├── dev.txt                    # Development requirements
│   ├── prod.txt                   # Production requirements
│   └── test.txt                   # Testing requirements
│
├── tests/                         # Test suite
│   ├── unit/
│   ├── integration/
│   ├── fixtures/
│   ├── conftest.py
│   └── pytest.ini
│
├── docker-compose.yml             # Local development stack
├── docker-compose.prod.yml        # Production stack (planned)
├── .dockerignore                  # Docker ignore file
├── .env.example                   # Environment variables template
├── .gitignore                     # Git ignore file
├── manage.py                      # Django management script
├── README.md                      # This file
└── setup.py                       # Package setup configuration
```

---

## Requirements

- **Python**: 3.13+
- **Django**: 6.0.5
- **Docker**: Latest version
- **Docker Compose**: Latest version
- **PostgreSQL**: 14+ (for production)
- **Redis**: 7+ (for caching and tasks)

---

## Installation & Setup

### 1. Prerequisites

Ensure you have the following installed:
- Python 3.13+
- Docker and Docker Compose
- Git

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/smartstock-ai.git
cd smartstock-ai
```

### 3. Create Environment File

```bash
cp .env.example .env
```

Edit `.env` with your local configuration:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 4. Setup Virtual Environment (Development)

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements/dev.txt
```

### 6. Run Migrations

```bash
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
# Follow prompts to create admin account
```

### 8. Load Sample Data (Optional)

```bash
python manage.py loaddata fixtures/sample_data.json
```

### 9. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 10. Start Development Server

```bash
python manage.py runserver
```

Access the application:
- **Frontend**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **API**: http://localhost:8000/api/v1

---

## Docker Setup (Recommended)

### Development with Docker

```bash
# Build and start containers
docker-compose up -d

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Run migrations
docker-compose exec web python manage.py migrate

# Access application
# Frontend: http://localhost:8000
# Admin: http://localhost:8000/admin
```

### Stop Containers

```bash
docker-compose down
```

---

## API Documentation

### Available Endpoints (Current)

#### Products
- `GET /api/v1/products/` - List all products
- `POST /api/v1/products/` - Create product (planned)
- `GET /api/v1/products/<id>/` - Get product details (planned)
- `PUT /api/v1/products/<id>/` - Update product (planned)
- `DELETE /api/v1/products/<id>/` - Delete product (planned)

#### Customers
- `GET /api/v1/customers/` - List all customers (planned)
- `POST /api/v1/customers/` - Create customer (planned)

#### Bills
- `GET /api/v1/bills/` - List all bills (planned)
- `POST /api/v1/bills/` - Create bill (planned)
- `GET /api/v1/bills/<id>/` - Get bill details (planned)

#### Reports
- `GET /api/v1/reports/sales/` - Sales report (planned)
- `GET /api/v1/reports/inventory/` - Inventory report (planned)

---

## Testing

### Run All Tests

```bash
pytest
```

### Run Specific Test Suite

```bash
pytest tests/unit/
pytest tests/integration/
```

### Run with Coverage

```bash
pytest --cov=apps --cov-report=html
```

---

## Development Guidelines

### Code Style

- Follow PEP 8
- Use Black for formatting
- Use isort for imports
- Maximum line length: 100 characters

### Format Code

```bash
black .
isort .
```

### Lint Code

```bash
flake8 apps/ core/
```

---

## Features Roadmap

### Phase 1 (Current)
- ✅ Product management
- ✅ Customer management
- ✅ Billing system
- ✅ Basic dashboard
- ✅ Admin interface

### Phase 2 (Q3 2026)
- ⏳ REST API implementation
- ⏳ React frontend
- ⏳ Advanced analytics
- ⏳ PDF invoice export
- ⏳ Email notifications

### Phase 3 (Q4 2026)
- ⏳ AI/ML features
- ⏳ Multi-tenancy support
- ⏳ Mobile app
- ⏳ Advanced reporting
- ⏳ Third-party integrations

### Phase 4 (2027)
- ⏳ SaaS deployment
- ⏳ Payment gateway integration
- ⏳ Advanced security features
- ⏳ Performance optimization

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add your feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit a pull request

---

## Database Models

### Products App
- **Category**: Product categories with descriptions
- **Product**: Main product model with pricing, stock, and status

### Customers App
- **Customer**: Customer information with contact details

### Billing App
- **Bill**: Invoice/bill records with automatic calculations
- **BillItem**: Individual line items in bills

### Accounts App (Future)
- **User**: Custom user model with extended fields
- **UserProfile**: Additional user information

---

## Troubleshooting

### Database Errors

```bash
# Reset database
rm db.sqlite3
python manage.py migrate

# Fresh migration
python manage.py makemigrations
python manage.py migrate
```

### Static Files Issues

```bash
# Recollect static files
python manage.py collectstatic --clear --noinput
```

### Port Already in Use

```bash
# Use different port
python manage.py runserver 8001
```

---

## License

MIT License - see LICENSE file for details

---

## Contact & Support

- **Project Lead**: Your Name
- **Email**: your.email@example.com
- **LinkedIn**: linkedin.com/in/yourprofile

---

## Acknowledgments

- Django community for excellent framework
- Bootstrap team for responsive design
- Chart.js for data visualization
- All contributors and supporters

---

**Last Updated**: May 16, 2026
**Current Version**: 1.0.0
**Status**: Active Development
- Top products by sales
- Sales statistics

## API Endpoints

### Authentication
- `POST /accounts/register/` - User registration
- `POST /accounts/login/` - User login
- `GET /accounts/logout/` - User logout

### Products
- `GET /products/` - List all products
- `POST /products/create/` - Create new product
- `GET /products/<id>/edit/` - Edit product
- `POST /products/<id>/delete/` - Delete product
- `GET /products/low-stock/` - View low stock items

### Customers
- `GET /customers/` - List all customers
- `POST /customers/create/` - Create new customer
- `GET /customers/<id>/` - View customer details
- `GET /customers/<id>/edit/` - Edit customer

### Billing
- `GET /billing/` - List all bills
- `POST /billing/create/` - Create new bill
- `GET /billing/<id>/` - View bill details
- `GET /billing/<id>/edit/` - Edit bill

### Reports
- `GET /reports/sales/` - View sales report

## Database Models

### Product
- name
- sku (unique)
- category
- description
- price
- stock_quantity
- reorder_level
- status

### Customer
- name
- email (unique)
- phone
- address
- city
- state
- postal_code
- country

### Bill
- bill_number (unique)
- customer (FK)
- total_amount
- status
- notes
- created_at
- updated_at

### BillItem
- bill (FK)
- product (FK)
- quantity
- price

## Settings Configuration

Key settings in `inventory_system/settings.py`:

- `DEBUG` - Set to False in production
- `ALLOWED_HOSTS` - Configure for your domain
- `DATABASES` - Database configuration
- `INSTALLED_APPS` - Installed applications
- `TEMPLATES` - Template configuration

## Security

- Enable HTTPS in production
- Set `DEBUG = False` in production
- Use strong `SECRET_KEY`
- Configure `ALLOWED_HOSTS`
- Use environment variables for sensitive data
- Regular security updates

## Development

### Create migrations:
```bash
python manage.py makemigrations
```

### Apply migrations:
```bash
python manage.py migrate
```

### Access Django admin:
```
http://localhost:8000/admin/
```

## Deployment

For production deployment:

1. Use a production WSGI server (Gunicorn, uWSGI)
2. Configure a reverse proxy (Nginx)
3. Use a production database (PostgreSQL)
4. Enable HTTPS/SSL
5. Set `DEBUG = False`
6. Configure proper logging
7. Set up regular backups

## Support

For issues and feature requests, please create an issue in the repository.

## License

This project is licensed under the MIT License.
