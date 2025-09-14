#!/bin/bash

# Specify results and generated directories
export RESULTS_DIR=results/dilithium5_times
export GENERATED_DIR=results/dilithium5_generated

# Commands used by time_generic.sh
export GEN_CMD="./openssl genpkey -provider default -provider oqsprovider -algorithm p521_mldsa87 -out $GENERATED_DIR/private.key"
export PUB_CMD="./openssl pkey -in $GENERATED_DIR/private.key -pubout -out $GENERATED_DIR/public.key -provider default -provider oqsprovider"
export CSR_CMD="./openssl req -new -key $GENERATED_DIR/private.key -out $GENERATED_DIR/request.csr -subj \"/C=US/ST=Georgia/L=Atlanta/O=My Company Inc/CN=mycompany.com\" -provider default -provider oqsprovider"
export SIGN_CMD="./openssl x509 -req -days 365 -in $GENERATED_DIR/request.csr -signkey $GENERATED_DIR/private.key -out $GENERATED_DIR/certificate.crt -provider default -provider oqsprovider"
export VERIFY_CMD="./openssl x509 -in $GENERATED_DIR/certificate.crt -text -noout -provider default -provider oqsprovider"

# Call the timing function script
exec "$(dirname "$0")/time_generic.sh"
