#!/bin/bash

# This script starts the Python benchmark script in the background
# and ensures it keeps running even after the shell is closed.

set -euo pipefail

LOG_FILE="run_benchmarks.log"

echo "Starting benchmark script in the background..."
NO_COLOR=1 nohup python3 -u run_benchmarks.py > "$LOG_FILE" 2>&1 &
PID=$!
echo "Script started with PID $PID"
echo "Combined stdout/stderr is being written to $LOG_FILE"
