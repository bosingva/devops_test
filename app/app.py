from flask import Flask
import requests

app = Flask(__name__)

WORKER_URL = "http://worker:5001/process"

@app.route("/")
def home():
    return "App is running"

@app.route("/task")
def send_task():
    try:
        r = requests.get(WORKER_URL)
        return f"Worker response: {r.text}"
    except Exception as e:
        return f"Error contacting worker: {str(e)}"

app.run(host="0.0.0.0", port=5000)