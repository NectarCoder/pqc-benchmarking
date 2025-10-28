#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# LESS family test wrapper — delegates to the generic harness.

VARIANTS=(
	less252192
	less25268
	less25245
	less400220
	less400102
	less548345
	less548137
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" LESS "${VARIANTS[@]}"
