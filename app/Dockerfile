FROM python:3.11-slim

WORKDIR /app

# Installing system dependencies before Python dependencies.
# Keeping them separate means apt layer is cached independently.
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py entrypoint.sh init.sh ./

RUN useradd -m appuser \
    && chown -R appuser:appuser /app \
    && chmod +x entrypoint.sh init.sh
    
USER appuser

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]