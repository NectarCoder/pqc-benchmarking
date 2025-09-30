#!/usr/bin/bash

# Specify results and generated directories
export TIMING_RESULTS_DIR=results/perk128short3_times
export MEMORY_RESULTS_DIR=results/perk128short3_memory
export GENERATED_DIR=results/perk128short3_generated

# Commands used to generate keys, CSRs, and certificates using OpenSSL via oqs-provider
export GEN_CMD="./openssl genpkey -provider default -provider oqsprovider -algorithm perk128short3 -out $GENERATED_DIR/private.key"
export PUB_CMD="./openssl pkey -in $GENERATED_DIR/private.key -pubout -out $GENERATED_DIR/public.key -provider default -provider oqsprovider"
export CSR_CMD="./openssl req -new -key $GENERATED_DIR/private.key -out $GENERATED_DIR/request.csr -subj \"/C=US/ST=Georgia/L=Atlanta/O=My Company Inc/CN=mycompany.com\" -provider default -provider oqsprovider"
export SIGN_CMD="./openssl x509 -req -days 365 -in $GENERATED_DIR/request.csr -signkey $GENERATED_DIR/private.key -out $GENERATED_DIR/certificate.crt -provider default -provider oqsprovider"
export VERIFY_CMD="./openssl verify -provider default -provider oqsprovider -CAfile $GENERATED_DIR/certificate.crt $GENERATED_DIR/certificate.crt"

# Call the metrics calculation script
"$(dirname "$0")/record_metrics.sh"
