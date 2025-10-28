#!/usr/bin/env bash

# MIRATH family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	mirathtcith1ashort
	mirathtcith1bshort
	mirathtcith3ashort
	mirathtcith3bshort
	mirathtcith5ashort
	mirathtcith5bshort
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" MIRATH "${VARIANTS[@]}"
