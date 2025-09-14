#!/bin/bash

# Specify results and generated directories
export RESULTS_DIR=results/rsa_times
export GENERATED_DIR=results/rsa_generated

# Commands used by time_generic.sh
export GEN_CMD="./openssl genrsa -out $GENERATED_DIR/private.key 2048"
export PUB_CMD="./openssl rsa -in $GENERATED_DIR/private.key -pubout -out $GENERATED_DIR/public.key"
export CSR_CMD="./openssl req -new -key $GENERATED_DIR/private.key -out $GENERATED_DIR/request.csr -subj \"/C=US/ST=Georgia/L=Atlanta/O=My Company Inc/CN=mycompany.com\""
export SIGN_CMD="./openssl x509 -req -days 365 -in $GENERATED_DIR/request.csr -signkey $GENERATED_DIR/private.key -out $GENERATED_DIR/certificate.crt"
export VERIFY_CMD="./openssl verify -CAfile $GENERATED_DIR/certificate.crt $GENERATED_DIR/certificate.crt"

# Call the timing function script
exec "$(dirname "$0")/time_generic.sh"
