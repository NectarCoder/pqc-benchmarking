#!/bin/bash

# This script starts the Python benchmark script in the background
# and ensures it keeps running even after the shell is closed.

echo "Starting benchmark script in the background..."
nohup python3 run_benchmarks.py > run_benchmarks.out 2> run_benchmarks.err &
echo "Script started. Output will be in run_benchmarks.out, errors in run_benchmarks.err"
