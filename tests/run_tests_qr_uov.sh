#!/usr/bin/env bash

# QR-UOV family test wrapper — delegates to the generic harness.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VARIANTS=(
	qruov1q127L3v156m54
	qruov1q7L10v740m100
	qruov1q31L3v165m60
	qruov1q31L10v600m70
	qruov3q127L3v228m78
	qruov3q7L10v1100m140
	qruov3q31L3v246m87
	qruov3q31L10v890m100
	qruov5q127L3v306m105
	qruov5q7L10v1490m190
	qruov5q31L3v324m114
	qruov5q31L10v1120m120
)

exec "$SCRIPT_DIR/test_algorithm_family.sh" "QR-UOV" "${VARIANTS[@]}"
