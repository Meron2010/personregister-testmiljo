FROM python:3.9-slim

WORKDIR /app

# Copy application code
COPY app.py test_anonymiserings.py clear_data.py ./

# Create directory for SQLite database
RUN mkdir -p /app/data

# Optional: install sqlite3 CLI (Python module is enough)
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Use a volume for persistent database
VOLUME ["/app/data"]

# Default command: run the app interactively
CMD ["python", "app.py"]

