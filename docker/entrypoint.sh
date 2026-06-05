#!/bin/bash
# Docker entrypoint script

set -e

# Run migrations
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@smartstock.com', 'admin123')
    print('Superuser created')
END

# Start the server
exec "$@"
