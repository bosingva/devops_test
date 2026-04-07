#!/bin/bash
set -e

# Step 1: startup message
echo "Starting App Container..."

# Step 2: run the separate init script
bash /app/init.sh

# Step 3: start the application
echo "Application started"
exec python app.py