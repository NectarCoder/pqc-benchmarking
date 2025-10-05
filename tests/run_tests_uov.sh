#!/usr/bin/env bash

# UOV family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	OV_Is
	OV_Ip
	OV_III
	OV_V
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" UOV "${VARIANTS[@]}"
