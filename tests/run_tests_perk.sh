#!/usr/bin/env bash

# PERK family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	perkak1short
	perkaesaes1short
	perkkeccakkeccak1short
	perkak3short
	perkaesaes3short
	perkkeccakkeccak3short
	perkak5short
	perkaesaes5short
	perkkeccakkeccak5short
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" PERK "${VARIANTS[@]}"
