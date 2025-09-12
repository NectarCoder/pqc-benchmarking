#!/bin/bash

# Clone oqs-provider repo
git clone https://github.com/open-quantum-safe/oqs-provider.git

# Run the fullbuild script to setup the benchmarking environment
echo "***** RUNNING OQS-PROVIDER FULLBUILD SCRIPT *****"
cd oqs-provider
chmod +x scripts/fullbuild.sh
OPENSSL_BRANCH=master LIBOQS_BRANCH=main MAKE_PARAMS="-j$(nproc)" scripts/fullbuild.sh -F
echo; echo; echo "***** OQS-PROVIDER FULLBUILD SCRIPT COMPLETE *****"
echo "***** VERIFY THAT NO ERRORS HAVE OCCURRED *****"; echo; echo;

# Verify OpenSSL installation succeeded
echo "Verifying OpenSSL installation..."
./.local/bin/openssl version; echo;

# Verify liboqs installation succeeded
echo "Verifying liboqs installation..."
grep '^Version:' ./.local/lib64/pkgconfig/liboqs.pc; echo;

# Set env variable to point to OpenSSL the location of the oqsprovider module
export OPENSSL_MODULES=$PWD/_build/lib

# Check if oqsprovider module exists
echo "Checking for oqsprovider module..."
if [ -f $OPENSSL_MODULES/oqsprovider.so ]; then
    echo "oqsprovider module found."
else
    echo "oqsprovider module not found."
fi; echo;

# Verify oqsprovider installation succeeded
echo "Verifying oqsprovider installation..."
./.local/bin/openssl list -providers -provider oqsprovider -provider-path $OPENSSL_MODULES
echo

echo "Verifying default (OpenSSL) provider installation..."
./.local/bin/openssl list -providers
echo

# Print completion message
echo; echo "***** OQS-PROVIDER, LIBOQS, AND OPENSSL SETUP COMPLETE *****"
echo "***** ENSURE ALL VERIFICATIONS ARE SUCCESSFUL *****"
echo "You can now use the local OpenSSL wrapper from the project root with ./openssl"
echo "Run ./openssl-help for usage information"
echo; echo
