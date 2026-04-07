# DevOps Engineer Technical Task

## Overview

This assignment evaluates your knowledge of:

* Docker
* Container networking
* Custom Docker entrypoints
* Basic service communication
* CI/CD pipelines
* Building Docker images

The goal is to run a small multi-container application and configure a CI pipeline that builds the Docker image.

---

# Project Description

The system consists of **two services**:

1. **App service**

   * A simple Python API
   * Sends tasks to a worker

2. **Worker service**

   * Processes tasks
   * Logs results

Both services must communicate using Docker networking.

---

# Requirements

You must complete the following tasks:

## 1. Build Docker Images

Create Dockerfiles for the services:

### App Container

Must:

* Run Python - Initial Dockerfile already provided with the desired docker image.
* Install dependencies (from the requirements file)
* Use a **custom entrypoint script** (see step number 2)
* Start the API server

### Worker Container

Must:

* Run a Python script (install dependencies if needed)
* Receive messages from the app

---

## 2. Custom Entrypoint

The **app container must run using a custom entrypoint script**.
Use bash for the entry point script

The script should:

1. Print a startup message
2. Run a startup script
3. Start the application

Example expected output:

```
Starting App Container...
Running initialization script...
Application started
```

---

## 3. Docker Compose

Create a `docker-compose.yml` file that:

* Runs both containers
* Connects them on the same network
* Ensures the worker container starts before the app

Expected services:

```
app
worker
```

The app should be able to reach the worker using the hostname:

```
http://worker:5001
```

---

## 4. Application Behavior

When calling:

```
http://localhost:5000/task
```

The app should send a task to the worker.

The worker should log something like:

```
Worker received task
Processing task...
Task completed
```

---

# CI/CD Pipeline

Create a CI pipeline that runs when code is merged into the **main branch**.

The pipeline must:

1. Checkout the repository
2. Build the Docker image for the app
3. Save the built image as a **pipeline artifact**

Example artifact:

```
app-image.tar
```

You may use any CI system such as:

* GitHub Actions
* GitLab CI
* Bitbucket Pipelines

---

# Deliverables

Please submit:

1. Completed Dockerfiles
2. docker-compose.yml
3. Entrypoint script
4. CI pipeline file

The project must run with:

```
docker-compose up --build
```

---

# Bonus (Optional)

* Add logging for the worker mounted to a specific dir.
* Add redis server in between the apps so the message will go through the redis.

---
