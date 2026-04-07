import os
import json
import redis
import logging as python_logging
import threading
from flask import Flask, jsonify

LOG_DIR = os.getenv("LOG_DIR", "/logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging = python_logging.getLogger(__name__)
python_logging.basicConfig(
    level=python_logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        python_logging.FileHandler(f"{LOG_DIR}/worker.log"),
        python_logging.StreamHandler(),
    ],
)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

health_app = Flask(__name__)
python_logging.getLogger('werkzeug').setLevel(python_logging.ERROR)

@health_app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "running", "service": "worker"}), 200

@health_app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


def run_health_server():
    health_app.run(host="0.0.0.0", port=5001, use_reloader=False)


threading.Thread(target=run_health_server, daemon=True).start()

logging.info("Worker started — waiting for tasks on queue 'tasks'")

while True:
    result = r.blpop("tasks", timeout=0)
    if result is None:
        continue

    _, raw = result
    try:
        data = json.loads(raw)
        task = data.get("task", "unknown")
        logging.info("Worker received task")
        logging.info(f"Processing task: {task}")
        logging.info("Task completed")
    except Exception as e:
        logging.error(f"Failed to process task: {e}")