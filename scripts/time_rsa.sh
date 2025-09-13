#!/bin/bash

echo -e "\nTIMING SCRIPT MUST BE RUN FROM PROJECT ROOT, OR OPENSSL WILL NOT WORK!"; echo;

# Create results directory if it doesn't exist, or clear it if it does
# - Store timing results in rsa_times/
# - Store generated files (keys, csr, certs) in rsa_generated/
for dir in results/rsa_times results/rsa_generated; do
    if [ -d "$dir" ]; then
        rm -rf "$dir"/*
    else
        mkdir -p "$dir"
    fi
done
export RESULTS_DIR=results/rsa_times/
export GENERATED_DIR=results/rsa_generated/
echo "Results directory is $RESULTS_DIR"
echo "Generated files directory is $GENERATED_DIR"

# Calculate private key generation time
(time ./openssl genrsa -out $GENERATED_DIR/private.key 2048) 2>> $RESULTS_DIR/time_private.txt

# Calculate public key extraction time
(time ./openssl rsa -in $GENERATED_DIR/private.key -pubout -out $GENERATED_DIR/public.key) 2>> $RESULTS_DIR/time_public.txt

# Calculate CSR creation time
(time ./openssl req -new -key $GENERATED_DIR/private.key -out $GENERATED_DIR/request.csr -subj "/C=US/ST=Georgia/L=Atlanta/O=My Company Inc/CN=mycompany.com") 2>> $RESULTS_DIR/time_csr.txt

# Calculate certificate signing time
(time ./openssl x509 -req -days 365 -in $GENERATED_DIR/request.csr -signkey $GENERATED_DIR/private.key -out $GENERATED_DIR/certificate.crt) 2>> $RESULTS_DIR/time_cert.txt

# Calculate certificate verification time
(time ./openssl verify -CAfile $GENERATED_DIR/certificate.crt $GENERATED_DIR/certificate.crt) 2>> $RESULTS_DIR/time_verify.txt

# Echo current security level to a file
echo "NIST_Security_Level, NA" >> $RESULTS_DIR/nist_level.txt

# Unset the results directory variable
unset RESULTS_DIR
unset GENERATED_DIR
