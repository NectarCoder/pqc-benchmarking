#!/usr/bin/env bash

# Standardized stub for family tests
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	hawk512
	hawk1024
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" HAWK "${VARIANTS[@]}"
