#!/bin/bash

echo -e "\nTIMING SCRIPT MUST BE RUN FROM PROJECT ROOT, OR OPENSSL WILL NOT WORK!"

# Create results directory if it doesn't exist
mkdir -p results/dilithium2_times/
export RESULTS_DIR=results/dilithium2_times/
echo "Results directory is $RESULTS_DIR"

# Calculate private key generation time
( time ./openssl genpkey -provider default -provider oqsprovider -algorithm p256_mldsa44 -out private.key ) > $RESULTS_DIR/time_private.txt

# Calculate public key extraction time
( time ./openssl pkey -in private.key -pubout -out public.key -provider default -provider oqsprovider ) > $RESULTS_DIR/time_public.txt

# Calculate CSR creation time
( time ./openssl req -new -key private.key -out request.csr -subj "/C=US/ST=Georgia/L=Atlanta/O=My Company Inc/CN=mycompany.com" -provider default -provider oqsprovider ) > $RESULTS_DIR/time_csr.txt

# Calculate certificate signing time
( time ./openssl x509 -req -days 365 -in request.csr -signkey private.key -out certificate.crt -provider default -provider oqsprovider ) > $RESULTS_DIR/time_cert.txt

# Calculate certificate verification time
( time ./openssl x509 -in certificate.crt -text -noout -provider default -provider oqsprovider ) > $RESULTS_DIR/time_verify.txt

# Unset the results directory variable
unset RESULTS_DIR

