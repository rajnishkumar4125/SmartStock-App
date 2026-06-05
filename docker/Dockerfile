FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements/prod.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r prod.txt

# Copy project files
COPY . .

# Create logs directory
RUN mkdir -p logs

# Collect static files
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

CMD ["gunicorn", "inventory_system.wsgi:application", "--bind", "0.0.0.0:8000"]
