#!/usr/bin/env bash

# PERK family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	perk128short3
	perk128short5
	perk192short3
	perk192short5
	perk256short3
	perk256short5
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" PERK "${VARIANTS[@]}"
