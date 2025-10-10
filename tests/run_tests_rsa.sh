#!/usr/bin/env bash

# RSA test harness.
# Usage: run_tests_rsa.sh
# It expects an OpenSSL wrapper at $OPENSSL or defaults to the repo-local ../openssl.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OPENSSL="${OPENSSL:-$REPO_ROOT/openssl}"

# Load centralized colors
. "$SCRIPT_DIR/colors.sh"

printf_info() { printf "%b[INFO]%b %s\n" "$COLOR_INFO" "$COLOR_RESET" "$*"; }
printf_ok() { printf "%b[OK]%b " "$COLOR_OK" "$COLOR_RESET"; printf "$@"; printf "\n"; }
printf_err() { printf "%b[ERR]%b " "$COLOR_ERR" "$COLOR_RESET"; printf "$@"; printf "\n"; }

die() {
    printf_err "ERROR: %s" "$*" >&2
}

printf "\n--- Testing RSA ---\n"

priv="rsa.private.key"
pub="rsa.public.key"
csr="rsa.request.csr"
crt="rsa.certificate.crt"

rm -f "$priv" "$pub" "$csr" "$crt"

set +e
errs=()

# 1) generate private key
if ! "$OPENSSL" genrsa -out "$priv" 2048 2>"rsa.genrsa.err"; then
    errs+=("genrsa failed: see rsa.genrsa.err")
fi

# 2) generate public key
if [ ${#errs[@]} -eq 0 ]; then
    if ! "$OPENSSL" rsa -in "$priv" -pubout -out "$pub" 2>"rsa.rsa.err"; then
        errs+=("rsa (pubout) failed: see rsa.rsa.err")
    fi
fi

# 3) create CSR
if [ ${#errs[@]} -eq 0 ]; then
    if ! "$OPENSSL" req -new -key "$priv" -out "$csr" -subj "/C=US/ST=Georgia/L=Atlanta/O=My Company Inc/CN=mycompany.com" 2>"rsa.req.err"; then
        errs+=("req (CSR) failed: see rsa.req.err")
    fi
fi

# 4) sign cert
if [ ${#errs[@]} -eq 0 ]; then
    if ! "$OPENSSL" x509 -req -days 365 -in "$csr" -signkey "$priv" -out "$crt" 2>"rsa.x509.err"; then
        errs+=("x509 (sign) failed: see rsa.x509.err")
    fi
fi

# 5) verify cert
if [ ${#errs[@]} -eq 0 ]; then
    if ! verify_out="$("$OPENSSL" verify -CAfile "$crt" "$crt" 2>&1)"; then
        echo "$verify_out" >"rsa.verify.err"
        errs+=("verify failed: see rsa.verify.err")
    else
        if ! echo "$verify_out" | grep -q "${crt}: OK"; then
            echo "$verify_out" >"rsa.verify.err"
            errs+=("verify unexpected output (see rsa.verify.err): $verify_out")
        fi
    fi
fi

# 6) display cert in human-readable form
if [ ${#errs[@]} -eq 0 ]; then
    if ! "$OPENSSL" x509 -in "$crt" -text -noout >"rsa.cert.text" 2>"rsa.x509.text.err"; then
        errs+=("x509 (text) failed: see rsa.x509.text.err")
    fi
fi

# Validate PEM contents
if [ ${#errs[@]} -eq 0 ]; then
    if ! grep -F -q -- "-----BEGIN PRIVATE KEY-----" "$priv" || ! grep -F -q -- "-----END PRIVATE KEY-----" "$priv"; then
        errs+=("private key PEM headers missing in $priv")
    fi
    if ! grep -F -q -- "-----BEGIN PUBLIC KEY-----" "$pub" || ! grep -F -q -- "-----END PUBLIC KEY-----" "$pub"; then
        errs+=("public key PEM headers missing in $pub")
    fi
    if ! grep -F -q -- "-----BEGIN CERTIFICATE REQUEST-----" "$csr" || ! grep -F -q -- "-----END CERTIFICATE REQUEST-----" "$csr"; then
        errs+=("CSR PEM headers missing in $csr")
    fi
    if ! grep -F -q -- "-----BEGIN CERTIFICATE-----" "$crt" || ! grep -F -q -- "-----END CERTIFICATE-----" "$crt"; then
        errs+=("certificate PEM headers missing in $crt")
    fi
fi

set -e

if [ ${#errs[@]} -eq 0 ]; then
    printf_ok "RSA: SUCCESS"
    # Cleanup generated files on success
    rm -f "$priv" "$pub" "$csr" "$crt"
    rm -f "rsa.genrsa.err" "rsa.rsa.err" "rsa.req.err" "rsa.x509.err" "rsa.verify.err" "rsa.x509.text.err" "rsa.cert.text"
    printf "\nRSA test: SUCCESSFUL\n\n"
    exit 0
else
    printf_err "RSA: FAILED"
    for e in "${errs[@]}"; do
        die "$e"
    done
    printf "\n"
    for ef in "rsa."*.err; do
        [ -f "$ef" ] || continue
        printf "\n===== Contents of %s =====\n" "$ef"
        sed -n '1,200p' "$ef" || true
    done
    printf "\nRSA test: FAILED\n\n"
    exit 1
fi
