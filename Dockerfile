# Use the official Python image
FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=5000
ENV FLASK_ENV=production  # default to production

# Install system dependencies (curl + build essentials)
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first to leverage caching
COPY requirements.txt .

# Install Python dependencies including Gunicorn
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn

# Copy the rest of the application
COPY . .

# Expose container port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

# Run app: dev mode uses Flask, prod uses Gunicorn
CMD if [ "$FLASK_ENV" = "development" ]; then \
        echo "Starting Flask dev server..."; \
        python app.py; \
    else \
        echo "Starting Gunicorn production server..."; \
        gunicorn --bind 0.0.0.0:${PORT} app:app --workers 3 \
                 --access-logfile - --error-logfile - --capture-output --log-level info; \
    fi
