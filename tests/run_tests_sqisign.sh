#!/usr/bin/env bash

# Standardized stub for family tests
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	sqisign353
	sqisign529
	sqisign701
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" SQISIGN "${VARIANTS[@]}"
