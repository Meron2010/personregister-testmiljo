# Use official Python slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY app.py .

# Create directory for SQLite database
RUN mkdir -p /data

# Install SQLite (optional, usually comes with Python, but ensures availability)
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Expose a port if needed (optional)
# EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
