#!/bin/bash

# Generic timing and memory recording helper for PQC benchmarking scripts.

# Usage: set the following environment variables before invoking this script:
#   TIMING_RESULTS_DIR  - directory to store timing statistics
#   MEMORY_RESULTS_DIR  - directory to store memory statistics
#   GENERATED_DIR       - directory to store generated artifacts
#   GEN_CMD             - command to generate the private key (should write private key to $GENERATED_DIR/private.key)
#   PUB_CMD             - command to extract public key (should read $GENERATED_DIR/private.key and write $GENERATED_DIR/public.key)
#   CSR_CMD             - command to create a CSR (should read private key and write $GENERATED_DIR/request.csr)
#   SIGN_CMD            - command to sign certificate (should read request.csr and write $GENERATED_DIR/certificate.crt)
#   VERIFY_CMD          - command to verify or inspect certificate (should read $GENERATED_DIR/certificate.crt)

set -euo pipefail

if [ -z "${TIMING_RESULTS_DIR:-}" ] || [ -z "${MEMORY_RESULTS_DIR:-}" ] || [ -z "${GENERATED_DIR:-}" ]; then
    echo "TIMING_RESULTS_DIR, MEMORY_RESULTS_DIR, and GENERATED_DIR must be set and non-empty" >&2
    exit 2
fi

# echo -e "\nSCRIPT MUST BE RUN FROM PROJECT ROOT, OR OPENSSL WILL NOT WORK!"; echo;

# Prepare directories
for dir in "$TIMING_RESULTS_DIR" "$MEMORY_RESULTS_DIR" "$GENERATED_DIR"; do
    if [ -d "$dir" ]; then
        rm -rf "$dir"/*
    else
        mkdir -p "$dir"
    fi
done

echo "Timing results directory is $TIMING_RESULTS_DIR"
echo "Memory results directory is $MEMORY_RESULTS_DIR"
echo "Generated files directory is $GENERATED_DIR"

# Save time output of a command to a results file
run_time() {
    local cmd="$1"
    local outfile="$2"

    # taskset - set single core processing (disable parallelism)
    # perf - collect timing information & cpu cycles
    { taskset -c 0 perf stat bash -c "$cmd"; } 2> "$TIMING_RESULTS_DIR/$outfile"
}

# Save memory usage (maximum resident set size) of a command to a results file
run_memory() {
    local cmd="$1"
    local outfile="$2"

    # /usr/bin/time -f "%M" - maximum resident set size in KB
    { /usr/bin/time -f "%M" bash -c "$cmd"; } 2> "$MEMORY_RESULTS_DIR/$outfile"
}

# Time the commands to create keys, CSRs, and certificates
run_time "$GEN_CMD" time_private.txt
run_time "$PUB_CMD" time_public.txt
run_time "$CSR_CMD" time_csr.txt
run_time "$SIGN_CMD" time_cert.txt
run_time "$VERIFY_CMD" time_verify.txt

# Cleanup generated files from the timing runs
rm -f "$GENERATED_DIR"/*

# Memory usage recording (RSS) for each command
run_memory "$GEN_CMD" mem_private.txt
run_memory "$PUB_CMD" mem_public.txt
run_memory "$CSR_CMD" mem_csr.txt
run_memory "$SIGN_CMD" mem_cert.txt
run_memory "$VERIFY_CMD" mem_verify.txt

# Cleanup exported vars (if caller exported them)
unset MEMORY_RESULTS_DIR
unset GENERATED_DIR
unset GEN_CMD
unset PUB_CMD
unset CSR_CMD
unset SIGN_CMD
unset VERIFY_CMD
