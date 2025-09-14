#!/bin/bash

# Generic timing helper for PQC benchmarking scripts.
# Usage: set the following environment variables before invoking this script:
#   RESULTS_DIR     - directory to store timing files (must end with /)
#   GENERATED_DIR   - directory to store generated artifacts (must end with /)
#   GEN_CMD         - command to generate the private key (should write private key to $GENERATED_DIR/private.key)
#   PUB_CMD         - command to extract public key (should read $GENERATED_DIR/private.key and write $GENERATED_DIR/public.key)
#   CSR_CMD         - command to create a CSR (should read private key and write $GENERATED_DIR/request.csr)
#   SIGN_CMD        - command to sign certificate (should read request.csr and write $GENERATED_DIR/certificate.crt)
#   VERIFY_CMD      - command to verify or inspect certificate (should read $GENERATED_DIR/certificate.crt)

set -euo pipefail

if [ -z "${RESULTS_DIR:-}" ] || [ -z "${GENERATED_DIR:-}" ]; then
    echo "RESULTS_DIR and GENERATED_DIR must be set and non-empty" >&2
    exit 2
fi

echo -e "\nTIMING SCRIPT MUST BE RUN FROM PROJECT ROOT, OR OPENSSL WILL NOT WORK!"; echo;

# Prepare directories
for dir in "$RESULTS_DIR" "$GENERATED_DIR"; do
    if [ -d "$dir" ]; then
        rm -rf "$dir"/*
    else
        mkdir -p "$dir"
    fi
done

echo "Results directory is $RESULTS_DIR"
echo "Generated files directory is $GENERATED_DIR"

# Helpers for running a command and appending the time output to a results file
run_time() {
    local cmd="$1"
    local outfile="$2"
    if [ -z "$cmd" ]; then
        echo "Skipping empty command for $outfile"
        return
    fi
    # Use bash -c so complex commands / pipes are supported
    { perf stat bash -c "$cmd"; } 2> "$RESULTS_DIR/$outfile"
}

# Run the configured commands. Each command is expected to operate on files in GENERATED_DIR
run_time "$GEN_CMD" time_private.txt
run_time "$PUB_CMD" time_public.txt
run_time "$CSR_CMD" time_csr.txt
run_time "$SIGN_CMD" time_cert.txt
run_time "$VERIFY_CMD" time_verify.txt

# Cleanup exported vars (if caller exported them)
unset RESULTS_DIR
unset GENERATED_DIR
unset GEN_CMD
unset PUB_CMD
unset CSR_CMD
unset SIGN_CMD
unset VERIFY_CMD
