#!/usr/bin/env bash

# Falcon family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	falcon512
	falcon1024
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" FALCON "${VARIANTS[@]}"
