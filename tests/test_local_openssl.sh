#!/usr/bin/env bash

# Check that the repo-local openssl wrapper (./openssl at repo root) works.
# Exit 0 on success, non-zero on failure.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

OPENSSL_WRAPPER="$REPO_ROOT/openssl"

. "$SCRIPT_DIR/colors.sh"

printf_info() { printf "%b[INFO]%b %s\n" "$COLOR_INFO" "$COLOR_RESET" "$*"; }
printf_ok() { printf "%b[OK]%b %s\n" "$COLOR_OK" "$COLOR_RESET" "$*"; }
printf_err() { printf "%b[ERR]%b %s\n" "$COLOR_ERR" "$COLOR_RESET" "$*"; }

printf_info "Checking repo-local OpenSSL wrapper: $OPENSSL_WRAPPER"

if [ ! -x "$OPENSSL_WRAPPER" ]; then
    printf_err "openss l wrapper not found or not executable at: $OPENSSL_WRAPPER"
    printf_err "Please build/install the local OpenSSL used by the tests (see scripts/install_pqc_openssl.sh)."
    printf "\n"
    exit 2
fi

# Try to run a minimal OpenSSL command that will fail fast if the binary is missing or broken.
# We use 'version' which prints version info and returns 0 on success.
if "$OPENSSL_WRAPPER" version >/dev/null 2>&1; then
    printf_ok "Local OpenSSL wrapper appears to be functional."
    # add a blank line for readability before proceeding
    printf "\n"
    exit 0
else
    printf_err "repo-local OpenSSL wrapper did not run successfully."
    printf_err "Run the repo setup/build (e.g. scripts/install_pqc_openssl.sh) to build OpenSSL."
    printf "\n"
    exit 3
fi
