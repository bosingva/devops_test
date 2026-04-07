import os
import json
import redis
from flask import Flask, jsonify

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


@app.route("/task", methods=["GET", "POST"])
def send_task():
    task = {"task": "This task was sent from app service/v1"}
    r.rpush("tasks", json.dumps(task))
    return jsonify({"status": "task queued", "queue": "tasks"}), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)