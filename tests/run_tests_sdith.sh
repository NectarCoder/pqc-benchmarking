#!/usr/bin/env bash

# SDITHCAT family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	sdithcat1short
	sdithcat3short
	sdithcat5short
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" SDITHCAT "${VARIANTS[@]}"
