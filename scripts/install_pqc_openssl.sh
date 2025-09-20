#!/usr/bin/bash

# Warn user that script must be run from the project root
echo -e "WARNING: THIS SCRIPT MUST BE RUN FROM THE PROJECT ROOT DIRECTORY"

# Init oqs-provider repo
rm -rf oqs-provider; git clone --branch 0.10.0 https://github.com/open-quantum-safe/oqs-provider.git

# Enable all algorithms (copy over modified generate.py)
cd oqs-provider/oqs-template
cp ../../scripts-py/generate.py generate.py
cd ..

# Clone liboqs - custom fork for more algorithms
rm -rf liboqs; git clone --branch ds-0.14.0-release https://github.com/NectarCoder/liboqs.git
# git clone --branch ds-0.14.0-release https://github.com/open-quantum-safe/liboqs.git

# Tell generator.py where liboqs is
export LIBOQS_SRC_DIR="$(pwd)/liboqs"
python3 oqs-template/generate.py

# Run the fullbuild script to setup the benchmarking environment
echo; echo "***** RUNNING OQS-PROVIDER FULLBUILD SCRIPT *****"
chmod +x scripts/fullbuild.sh
OPENSSL_BRANCH=openssl-3.5.3 MAKE_PARAMS="-j$(nproc)" scripts/fullbuild.sh -f
# OPENSSL_BRANCH=openssl-3.5 LIBOQS_BRANCH=ds-0.14.0-release MAKE_PARAMS="-j$(nproc)" scripts/fullbuild.sh -f
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

# Update git submodules
cd "$(dirname "${BASH_SOURCE[0]}")/.." # Change to project root
git submodule update --init --recursive

# Print completion message
echo; echo "***** OQS-PROVIDER, LIBOQS, AND OPENSSL SETUP COMPLETE *****"
echo "***** ENSURE ALL VERIFICATIONS ARE SUCCESSFUL *****"; echo;
echo "You can now use the local OpenSSL wrapper from the project root with ./openssl"
echo "Run ./openssl-help for usage information"
echo; echo
