#!/usr/bin/env bash

# Lightweight test-run dispatcher for algorithm-family test scripts.
# Accepts zero or one argument. With no argument, run all families.
# With one argument, the argument (case-insensitive) must match one
# of the allowed algorithm families and the corresponding
# run_tests_<family>.sh script will be executed.

set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Load centralized color variables (colors.sh sets variables only when appropriate)
. "$SCRIPT_DIR/colors.sh"

# Top gap for readability
printf "\n"

print_usage() {
	cat <<EOF
Usage: $(basename "$0") [ALGORITHM-FAMILY]

Where ALGORITHM-FAMILY is one of (case-insensitive):
  RSA, Dilithium, Sphincs, Falcon, CROSS, FAEST, HAWK,
  LESS, MAYO, Mirath, MQOM, PERK, QR-UOV, RYDE, SDitH,
  SNOVA, SQISign, UOV

If no ALGORITHM-FAMILY is provided, the script will attempt to run tests for ALL families.
Examples:
  $(basename "$0")                # run all families
  $(basename "$0") CROSS          # run CROSS tests only
  $(basename "$0") --help         # show this help

Dev Note: Each family maps to a separate script named run_tests_<family>.sh (example: CROSS -> run_tests_cross.sh).

EOF
}

# Ordered list of families for the "run all" mode (use uppercase keys).
FAMILIES=(
  RSA DILITHIUM FALCON SPHINCS MAYO CROSS UOV SNOVA PERK HAWK RYDE FAEST LESS MIRATH MQOM "QR-UOV" SDITH SQISIGN
)

# Mapping from canonical uppercase family token -> script filename
declare -A FAMILY_SCRIPT
FAMILY_SCRIPT["RSA"]="run_tests_rsa.sh"
FAMILY_SCRIPT["DILITHIUM"]="run_tests_dilithium.sh"
FAMILY_SCRIPT["FALCON"]="run_tests_falcon.sh"
FAMILY_SCRIPT["SPHINCS"]="run_tests_sphincs.sh"
FAMILY_SCRIPT["MAYO"]="run_tests_mayo.sh"
FAMILY_SCRIPT["CROSS"]="run_tests_cross.sh"
FAMILY_SCRIPT["UOV"]="run_tests_uov.sh"
FAMILY_SCRIPT["SNOVA"]="run_tests_snova.sh"
FAMILY_SCRIPT["PERK"]="run_tests_perk.sh"
FAMILY_SCRIPT["HAWK"]="run_tests_hawk.sh"
FAMILY_SCRIPT["RYDE"]="run_tests_ryde.sh"
FAMILY_SCRIPT["FAEST"]="run_tests_faest.sh"
FAMILY_SCRIPT["LESS"]="run_tests_less.sh"
FAMILY_SCRIPT["MIRATH"]="run_tests_mirath.sh"
FAMILY_SCRIPT["MQOM"]="run_tests_mqom.sh"
FAMILY_SCRIPT["QR-UOV"]="run_tests_qr_uov.sh"
FAMILY_SCRIPT["SDITH"]="run_tests_sdith.sh"
FAMILY_SCRIPT["SQISIGN"]="run_tests_sqisign.sh"

run_script() {
	local fam_key="$1"
	local script_name="${FAMILY_SCRIPT[$fam_key]}"
	local script_path="$SCRIPT_DIR/$script_name"

	printf "%b== Running family: %s ==%b\n" "$COLOR_HDR" "$fam_key" "$COLOR_RESET"

	if [ -f "$script_path" ]; then
		if [ -x "$script_path" ]; then
			"$script_path"
			return $?
		else
			# Try to run with bash if not executable
			bash "$script_path"
			return $?
		fi
	else
		printf "Skipping %s: %s not found in %s\n" "$fam_key" "$script_name" "$SCRIPT_DIR"
		return 127
	fi
}

# Before running any family tests, verify the local OpenSSL wrapper is functional.
check_local_openssl() {
	local check_script="$SCRIPT_DIR/test_local_openssl.sh"
	if [ -f "$check_script" ] && [ -x "$check_script" ]; then
		"$check_script" || {
			echo "Aborting: local OpenSSL check failed."
			exit 4
		}
	else
		echo "Warning: local OpenSSL check script not found or not executable: $check_script"
		echo "Proceeding without OpenSSL check."
	fi
}

if [ "$#" -gt 1 ]; then
	echo "Error: this script accepts at most one argument."
	print_usage
	exit 2
fi

if [ "$#" -eq 0 ]; then
	echo "No family specified — running all families."

	# Mark mode for per-family scripts (ALL means continue across variant failures)
	export RUN_TESTS_MODE="ALL"

	# Verify local OpenSSL wrapper is functional before running any tests
	check_local_openssl
	failures=()
	for fam in "${FAMILIES[@]}"; do
		# Normalize keys: remove quotes in array entries like "QR-UOV" and ensure uppercase
		fam_key="$fam"
		# Normalize common variations: allow 'SDitH' -> 'SDITH', 'SQISign' -> 'SQISIGN'
		fam_key_upper="$(printf '%s' "$fam_key" | tr '[:lower:]' '[:upper:]')"
		run_script "$fam_key_upper" || failures+=("$fam_key_upper")
	done

	if [ ${#failures[@]} -eq 0 ]; then
		printf "\n%bAll requested family scripts completed (or were present and ran).%b\n\n" "$COLOR_OK" "$COLOR_RESET"
		exit 0
	else
		printf "\n%bThe following families failed or were skipped:%b %s\n\n" "$COLOR_ERR" "$COLOR_RESET" "${failures[*]}"
		exit 1
	fi
else
	arg="$1"
	# help handling
	case "$arg" in
		-h|--help|-help)
			print_usage
			exit 0
			;;
	esac

	arg_up="$(printf '%s' "$arg" | tr '[:lower:]' '[:upper:]')"

	# Allow user to pass QR-UOV using qr-uov or qr_uov; normalize underscores to hyphen
	arg_up="${arg_up//_/-}"
	# Special-case to ensure QR-UOV maps correctly (handle QR-UOV, QR_UOV, QRUOV)
	if [[ "$arg_up" =~ ^QR.?UOV$ ]]; then
		arg_up="QR-UOV"
	fi

	# Special-case SDitH variations -> SDITH
	if [[ "${arg_up,,}" == "sdith" ]]; then
		arg_up="SDITH"
	fi

	if [ -z "${FAMILY_SCRIPT[$arg_up]+_set}" ]; then
		echo "Error: unknown family '$arg'"
		print_usage
		exit 2
	fi

	# Run single family
	# Single-family mode: per-family scripts should abort on first variant failure
	export RUN_TESTS_MODE="SINGLE"

	# Verify local OpenSSL wrapper is functional before running the single family test
	check_local_openssl
	run_script "$arg_up"
	exit $?
fi




