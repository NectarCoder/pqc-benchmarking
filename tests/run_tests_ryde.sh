#!/usr/bin/env bash

# RYDE family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	ryde1s
	ryde3s
	ryde5s
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" RYDE "${VARIANTS[@]}"
