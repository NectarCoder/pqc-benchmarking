#!/usr/bin/env bash

# Standardized stub for Sphincs family tests
set -euo pipefail

printf_info() { printf "[INFO] %s\n" "$*"; }
printf_ok() { printf "\x1b[32m[OK]\x1b[0m "; printf "$@"; printf "\n"; }
printf_err() { printf "\x1b[31m[ERR]\x1b[0m "; printf "$@"; printf "\n"; }

printf_info "TODO: run Sphincs family tests"
exit 0
