#!/usr/bin/env bash

# Dilithium family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	mldsa44
	mldsa65
	mldsa87
)

# Exec the generic harness: test_algorithm_family.sh <FAMILY_NAME> <VARIANT1> [VARIANT2 ...]
exec "$SCRIPT_DIR/test_algorithm_family.sh" DILITHIUM "${VARIANTS[@]}"
