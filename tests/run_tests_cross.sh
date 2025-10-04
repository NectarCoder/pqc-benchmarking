#!/usr/bin/env bash

# CROSS family tests: generate keypair, CSR, certificate, and verify for each variant.

set -euo pipefail

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Variants
VARIANTS=(
  CROSSrsdp128small
  CROSSrsdp192small
  CROSSrsdp256small
  CROSSrsdpg128small
  CROSSrsdpg192small
  CROSSrsdpg256small
)

# Delegate to the generic harness. It expects: <FAMILY_NAME> <VARIANT1> [VARIANT2 ...]
exec "$SCRIPT_DIR/test_algorithm_family.sh" CROSS "${VARIANTS[@]}"

