#!/bin/bash

echo -e "\nTIMING SCRIPT MUST BE RUN FROM PROJECT ROOT, OR OPENSSL WILL NOT WORK!"; echo;

# Create results directory if it doesn't exist
# - Under results/, create dilithium3_times/ and dilithium3_generated/
# - Store timing results in dilithium3_times/
# - Store generated files (keys, csr, certs) in dilithium3_generated/
mkdir -p results/dilithium3_times/
mkdir -p results/dilithium3_generated/
export RESULTS_DIR=results/dilithium3_times/
export GENERATED_DIR=results/dilithium3_generated/
echo "Results directory is $RESULTS_DIR"
echo "Generated files directory is $GENERATED_DIR"

# Calculate private key generation time
(time ./openssl genpkey -provider default -provider oqsprovider -algorithm p384_mldsa65 -out $GENERATED_DIR/private.key) 2>> $RESULTS_DIR/time_private.txt

# Calculate public key extraction time
(time ./openssl pkey -in $GENERATED_DIR/private.key -pubout -out $GENERATED_DIR/public.key -provider default -provider oqsprovider) 2>> $RESULTS_DIR/time_public.txt

# Calculate CSR creation time
(time ./openssl req -new -key $GENERATED_DIR/private.key -out $GENERATED_DIR/request.csr -subj "/C=US/ST=Georgia/L=Atlanta/O=My Company Inc/CN=mycompany.com" -provider default -provider oqsprovider) 2>> $RESULTS_DIR/time_csr.txt

# Calculate certificate signing time
(time ./openssl x509 -req -days 365 -in $GENERATED_DIR/request.csr -signkey $GENERATED_DIR/private.key -out $GENERATED_DIR/certificate.crt -provider default -provider oqsprovider) 2>> $RESULTS_DIR/time_cert.txt

# Calculate certificate verification time
(time ./openssl x509 -in $GENERATED_DIR/certificate.crt -text -noout -provider default -provider oqsprovider) 2>> $RESULTS_DIR/time_verify.txt

# Echo current security level to a file
echo "NIST_Security_Level, 3" >> $RESULTS_DIR/nist_level.txt

# Unset the results directory variable
unset RESULTS_DIR
unset GENERATED_DIR
