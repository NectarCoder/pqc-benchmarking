#!/usr/bin/env bash

# Standardized stub for family tests
set -euo pipefail

printf_info() { printf "[INFO] %s\n" "$*"; }
printf_ok() { printf "\x1b[32m[OK]\x1b[0m "; printf "$@"; printf "\n"; }
printf_err() { printf "\x1b[31m[ERR]\x1b[0m "; printf "$@"; printf "\n"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	hawk512
	hawk1024
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" HAWK "${VARIANTS[@]}"
