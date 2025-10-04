#!/usr/bin/env bash

# Standardized stub for family tests
set -euo pipefail

printf_info() { printf "[INFO] %s\n" "$*"; }
printf_ok() { printf "\x1b[32m[OK]\x1b[0m %s\n" "$*"; }
printf_err() { printf "\x1b[31m[ERR]\x1b[0m %s\n" "$*"; }

family="$(basename "$0" | sed -e 's/^run_tests_//' -e 's/\.sh$//' -e 's/_/\-/g')"
printf_info "TODO: run ${family} family tests"
exit 0
