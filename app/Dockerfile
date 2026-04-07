FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py entrypoint.sh init.sh ./

RUN useradd -m appuser \
    && chown -R appuser:appuser /app \
    && chmod +x entrypoint.sh init.sh
    
USER appuser

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]