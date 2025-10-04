#!/usr/bin/env bash

# Generic algorithm-family test harness.
# Usage: test_algorithm_family.sh <FAMILY_NAME> <VARIANT1> [VARIANT2 ...]
# It expects an OpenSSL wrapper at $OPENSSL or defaults to the repo-local ../openssl.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OPENSSL="${OPENSSL:-$REPO_ROOT/openssl}"

# Mode behavior: RUN_TESTS_MODE exported by dispatcher (ALL or SINGLE)
RUN_MODE="${RUN_TESTS_MODE:-SINGLE}"

# Load centralized colors
. "$SCRIPT_DIR/colors.sh"

printf_info() { printf "%b[INFO]%b %s\n" "$COLOR_INFO" "$COLOR_RESET" "$*"; }
printf_ok() { printf "%b[OK]%b " "$COLOR_OK" "$COLOR_RESET"; printf "$@"; printf "\n"; }
printf_err() { printf "%b[ERR]%b " "$COLOR_ERR" "$COLOR_RESET"; printf "$@"; printf "\n"; }

# Note: top gap is handled by dispatcher; don't print an extra leading newline here.

die() {
    printf_err "ERROR: %s" "$*" >&2
}

if [ "$#" -lt 2 ]; then
    printf_err "Usage: %s <FAMILY_NAME> <VARIANT1> [VARIANT2 ...]" "$(basename "$0")"
    exit 2
fi

FAMILY_NAME="$1"
shift
VARIANTS=("$@")

run_variant() {
    local alg="$1"
    local prefix="${alg}"
    local priv="${prefix}.private.key"
    local pub="${prefix}.public.key"
    local csr="${prefix}.request.csr"
    local crt="${prefix}.certificate.crt"

    printf "\n--- Testing variant: %s ---\n" "$alg"

    rm -f "$priv" "$pub" "$csr" "$crt"

    set +e
    errs=()

    # 1) generate private key
    if ! "$OPENSSL" genpkey -provider default -provider oqsprovider -algorithm "$alg" -out "$priv" 2>"${prefix}.genpkey.err"; then
        errs+=("genpkey failed: see ${prefix}.genpkey.err")
    fi

    # 2) generate public key
    if [ ${#errs[@]} -eq 0 ]; then
        if ! "$OPENSSL" pkey -in "$priv" -pubout -out "$pub" -provider default -provider oqsprovider 2>"${prefix}.pkey.err"; then
            errs+=("pkey (pubout) failed: see ${prefix}.pkey.err")
        fi
    fi

    # 3) create CSR
    if [ ${#errs[@]} -eq 0 ]; then
        if ! "$OPENSSL" req -new -key "$priv" -out "$csr" -subj "/C=US/ST=Georgia/L=Atlanta/O=My Company Inc/CN=mycompany.com" -provider default -provider oqsprovider 2>"${prefix}.req.err"; then
            errs+=("req (CSR) failed: see ${prefix}.req.err")
        fi
    fi

    # 4) sign cert
    if [ ${#errs[@]} -eq 0 ]; then
        if ! "$OPENSSL" x509 -req -days 365 -in "$csr" -signkey "$priv" -out "$crt" -provider default -provider oqsprovider 2>"${prefix}.x509.err"; then
            errs+=("x509 (sign) failed: see ${prefix}.x509.err")
        fi
    fi

    # 5) verify cert
    if [ ${#errs[@]} -eq 0 ]; then
        if ! verify_out="$($OPENSSL verify -provider default -provider oqsprovider -CAfile "$crt" "$crt" 2>&1)"; then
            echo "$verify_out" >"${prefix}.verify.err"
            errs+=("verify failed: see ${prefix}.verify.err")
        else
            if ! echo "$verify_out" | grep -q "${crt}: OK"; then
                echo "$verify_out" >"${prefix}.verify.err"
                errs+=("verify unexpected output (see ${prefix}.verify.err): $verify_out")
            fi
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
        printf_ok "Variant %s: SUCCESS" "$alg"
        rm -f "$priv" "$pub" "$csr" "$crt"
        rm -f "${prefix}.genpkey.err" "${prefix}.pkey.err" "${prefix}.req.err" "${prefix}.x509.err" "${prefix}.verify.err"
        return 0
    else
        printf_err "Variant %s: FAILED" "$alg"
        for e in "${errs[@]}"; do
            die "$e"
        done
        printf "\n"
        for ef in "${prefix}."*.err; do
            [ -f "$ef" ] || continue
            printf "\n===== Contents of %s =====\n" "$ef"
            sed -n '1,200p' "$ef" || true
        done
        return 1
    fi
}

main() {
    overall_failures=()
    for v in "${VARIANTS[@]}"; do
        if run_variant "$v"; then
            :
        else
            overall_failures+=("$v")
            if [ "$RUN_MODE" = "SINGLE" ]; then
                printf_err "Aborting due to failure in SINGLE mode."
                return 2
            fi
        fi
    done

    if [ ${#overall_failures[@]} -eq 0 ]; then
        printf "\n%s family: ALL VARIANTS SUCCESSFUL\n\n" "$FAMILY_NAME"
        return 0
    else
        printf "\n%s family: failures: %s\n\n" "$FAMILY_NAME" "${overall_failures[*]}"
        return 1
    fi
}

main
