#!/usr/bin/env bash

# MQOM family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	mqom2cat1gf2shortr3
	mqom2cat1gf2shortr5
	mqom2cat1gf16shortr3
	mqom2cat1gf16shortr5
	mqom2cat1gf256shortr3
	mqom2cat1gf256shortr5
	mqom2cat3gf2shortr3
	mqom2cat3gf2shortr5
	mqom2cat3gf16shortr3
	mqom2cat3gf16shortr5
	mqom2cat3gf256shortr3
	mqom2cat3gf256shortr5
	mqom2cat5gf2shortr3
	mqom2cat5gf2shortr5
	mqom2cat5gf16shortr3
	mqom2cat5gf16shortr5
	mqom2cat5gf256shortr3
	mqom2cat5gf256shortr5
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" MQOM "${VARIANTS[@]}"
