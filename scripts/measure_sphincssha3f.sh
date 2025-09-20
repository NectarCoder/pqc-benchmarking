#!/usr/bin/bash

# Specify results and generated directories
export TIMING_RESULTS_DIR=results/sphincssha3f_times
export MEMORY_RESULTS_DIR=results/sphincssha3f_memory
export GENERATED_DIR=results/sphincssha3f_generated

# Commands used to generate keys, CSRs, and certificates using OpenSSL
export GEN_CMD="./openssl genpkey -algorithm slh-dsa-sha2-192f -out $GENERATED_DIR/private.key"
export PUB_CMD="./openssl pkey -in $GENERATED_DIR/private.key -pubout -out $GENERATED_DIR/public.key"
export CSR_CMD="./openssl req -new -key $GENERATED_DIR/private.key -out $GENERATED_DIR/request.csr -subj \"/C=US/ST=Georgia/L=Atlanta/O=My Company Inc/CN=mycompany.com\""
export SIGN_CMD="./openssl x509 -req -days 365 -in $GENERATED_DIR/request.csr -signkey $GENERATED_DIR/private.key -out $GENERATED_DIR/certificate.crt"
export VERIFY_CMD="./openssl verify -CAfile $GENERATED_DIR/certificate.crt $GENERATED_DIR/certificate.crt"

# Call the metrics calculation script
"$(dirname "$0")/record_metrics.sh"
