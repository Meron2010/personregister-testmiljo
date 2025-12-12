FROM python:3.9-slim

WORKDIR /app

COPY app.py test_gdpr.py ./

RUN mkdir -p /app/data

RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

VOLUME ["/app/data"]

CMD ["python", "test_gdpr.py"]
