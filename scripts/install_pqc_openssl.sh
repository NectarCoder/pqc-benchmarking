#!/bin/bash

# Init oqs-provider submodule
git pull
git submodule update --init --recursive

# Run the fullbuild script to setup the benchmarking environment
echo; echo "***** RUNNING OQS-PROVIDER FULLBUILD SCRIPT *****"
cd oqs-provider
chmod +x scripts/fullbuild.sh
OPENSSL_BRANCH=openssl-3.5 LIBOQS_BRANCH=ds-0.14.0-release MAKE_PARAMS="-j$(nproc)" scripts/fullbuild.sh -F
# OPENSSL_BRANCH=master LIBOQS_BRANCH=main MAKE_PARAMS="-j$(nproc)" scripts/fullbuild.sh -F
echo; echo; echo "***** OQS-PROVIDER FULLBUILD SCRIPT COMPLETE *****"
echo "***** VERIFY THAT NO ERRORS HAVE OCCURRED *****"; echo; echo;

# Verify OpenSSL installation succeeded
echo "Verifying OpenSSL installation..."
./.local/bin/openssl version; echo;

# Verify liboqs installation succeeded
echo "Verifying liboqs installation..."
grep '^Version:' ./.local/lib64/pkgconfig/liboqs.pc; echo;

# Point OpenSSL to the installed modules directory (contains default provider)
export OPENSSL_MODULES=$PWD/.local/lib64/ossl-modules

# Ensure oqsprovider module is available in the installed modules directory
echo "Checking for oqsprovider module..."
if [ -f $PWD/_build/lib/oqsprovider.so ]; then
    echo "Found built oqsprovider at _build/lib/oqsprovider.so"
    mkdir -p "$OPENSSL_MODULES"
    cp -f "$PWD/_build/lib/oqsprovider.so" "$OPENSSL_MODULES/"
else
    echo "oqsprovider not found at _build/lib/oqsprovider.so"
fi

if [ -f "$OPENSSL_MODULES/oqsprovider.so" ]; then
    echo "oqsprovider module present in $OPENSSL_MODULES."
else
    echo "oqsprovider module not present in $OPENSSL_MODULES."
fi; echo;

# Verify oqsprovider installation succeeded
echo "Verifying oqsprovider installation..."
./.local/bin/openssl list -providers -provider oqsprovider
echo

echo "Verifying default (OpenSSL) provider installation..."
./.local/bin/openssl list -providers
echo

# Print completion message
echo; echo "***** OQS-PROVIDER, LIBOQS, AND OPENSSL SETUP COMPLETE *****"
echo "***** ENSURE ALL VERIFICATIONS ARE SUCCESSFUL *****"; echo;
echo "You can now use the local OpenSSL wrapper from the project root with ./openssl"
echo "Run ./openssl-help for usage information"
echo; echo
