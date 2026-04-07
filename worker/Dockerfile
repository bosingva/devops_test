FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY worker.py .

RUN useradd -m workeruser \
    && mkdir -p /logs \
    && chown workeruser:workeruser /logs

USER workeruser

EXPOSE 5001

CMD ["python", "worker.py"]