#!/bin/bash

# Clone oqs-provider repo
git clone https://github.com/open-quantum-safe/oqs-provider.git

# Overwrite the fullbuild.sh script with our modified version
cp scripts/oqsprovider-fullbuild-modified.sh oqs-provider/scripts/fullbuild.sh

# Run the fullbuild script to setup the benchmarking environment
echo "**** RUNNING OQS-PROVIDER FULLBUILD SCRIPT ****"
cd oqs-provider/scripts
chmod +x fullbuild.sh
OPENSSL_BRANCH=master LIBOQS_BRANCH=main MAKE_PARAMS="-j$(nproc)" ./fullbuild.sh -F
echo "**** OQS-PROVIDER FULLBUILD SCRIPT COMPLETE ****"
echo "**** VERIFY THAT NO ERRORS HAVE OCCURRED ****"

# Verify OpenSSL installation succeeded
echo "Verifying OpenSSL installation..."
./../.local/bin/openssl version

# Verify liboqs installation succeeded
echo "Verifying liboqs installation..."
grep '^Version:' ../.local/lib/pkgconfig/liboqs.pc

# Set env variable to point to OpenSSL the location of the oqsprovider module
export OPENSSL_MODULES=$PWD/../_build/lib

# Verify oqsprovider installation succeeded
echo "Verifying oqsprovider installation..."
./../.local/bin/openssl list -providers -provider oqsprovider -provider-path ../_build/lib

echo "Verifying default (OpenSSL) provider installation..."
./../.local/bin/openssl list -providers

# Print completion message
echo; echo; echo "***** OQS-PROVIDER, LIBOQS, AND OPENSSL SETUP COMPLETE *****"
echo "You can now use the local OpenSSL wrapper from the project root with ./openssl"
echo "Run ./openssl-help for usage information"
echo; echo
