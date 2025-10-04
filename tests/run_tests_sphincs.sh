#!/usr/bin/env bash

# Sphincs family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	slh-dsa-sha2-128s
	slh-dsa-sha2-192s
	slh-dsa-sha2-256s
	slh-dsa-shake-128s
	slh-dsa-shake-192s
	slh-dsa-shake-256s
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" SPHINCS "${VARIANTS[@]}"
