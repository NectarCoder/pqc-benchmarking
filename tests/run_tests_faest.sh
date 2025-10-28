#!/usr/bin/env bash

# Standardized stub for family tests
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	faest128s
	faestem128s
	faest192s
	faestem192s
	faest256s
	faestem256s
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" FAEST "${VARIANTS[@]}"
