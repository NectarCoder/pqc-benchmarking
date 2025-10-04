#!/usr/bin/env bash

# Mayo family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	mayo1
	mayo2
	mayo3
	mayo5
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" MAYO "${VARIANTS[@]}"
