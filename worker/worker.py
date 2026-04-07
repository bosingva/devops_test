import os
import json
import redis
import logging

LOG_DIR = os.getenv("LOG_DIR", "/logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/worker.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

logger.info("Worker started — waiting for tasks on queue 'tasks'")

while True:
    # BLPOP blocks until a task arrives; timeout=0 means wait forever
    result = r.blpop("tasks", timeout=0)
    if result is None:
        continue

    _, raw = result
    try:
        data = json.loads(raw)
        task = data.get("task", "unknown")

        logger.info("Worker received task")
        logger.info(f"Processing task: {task}")
        logger.info("Task completed")

    except Exception as e:
        logger.error(f"Failed to process task: {e}")