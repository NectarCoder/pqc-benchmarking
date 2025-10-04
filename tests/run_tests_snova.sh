#!/usr/bin/env bash

# SNOVA family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	snova2454
	snova37172
	snova2583
	snova56252
	snova49113
	snova3784
	snova2455
	snova60104
	snova2965
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" SNOVA "${VARIANTS[@]}"
