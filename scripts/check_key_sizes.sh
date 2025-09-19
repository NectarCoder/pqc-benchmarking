#!/bin/bash

#
# A script to check the byte size of a private key, its corresponding
# public key, and a signature generated from it.
#
# Usage: ./check_key_sizes.sh /path/to/your_private_key
#

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Style and Color Configuration ---
BOLD=$(tput bold)
BLUE=$(tput setaf 4)
NORMAL=$(tput sgr0)

# --- 1. Argument and File Validation ---
if [ "$#" -ne 1 ]; then
    echo "Error: Incorrect number of arguments."
    echo "Usage: $0 <path_to_private_key>"
    exit 1
fi

PRIVATE_KEY_FILE="$1"

if [ ! -f "$PRIVATE_KEY_FILE" ]; then
    echo "Error: Private key file not found at '$PRIVATE_KEY_FILE'"
    exit 1
fi

# --- 2. Temporary File Setup & Cleanup ---
# Create temporary file names based on the script's process ID ($$) to avoid conflicts.
PUBLIC_KEY_FILE="temp_pub_key_$$.pem"
MESSAGE_FILE="temp_message_$$.txt"
SIGNATURE_FILE="temp_signature_$$.bin"

# The 'trap' command ensures that the specified command (rm -f) is executed
# when the script exits, whether it finishes successfully or fails.
# This guarantees our temporary files are always cleaned up.
trap 'rm -f "$PUBLIC_KEY_FILE" "$MESSAGE_FILE" "$SIGNATURE_FILE"' EXIT

echo -e "\nAnalyzing key: ${BOLD}${BLUE}${PRIVATE_KEY_FILE}${NORMAL}\n"

# --- 3. Perform Checks ---

# Check Private Key Size
echo "--- 🔐 Private Key ---"
priv_key_bytes=$(./openssl pkey -in "$PRIVATE_KEY_FILE" -provider default -provider oqsprovider -outform DER | wc -c)
echo "Size: ${BOLD}$priv_key_bytes bytes${NORMAL}"
echo

# Check Public Key Size
echo "--- 🔑 Public Key ---"
./openssl pkey -in "$PRIVATE_KEY_FILE" -provider default -provider oqsprovider -pubout -out "$PUBLIC_KEY_FILE" 2>/dev/null
pub_key_bytes=$(./openssl pkey -pubin -in "$PUBLIC_KEY_FILE" -provider default -provider oqsprovider -outform DER | wc -c)
echo "Size: ${BOLD}$pub_key_bytes bytes${NORMAL}"
echo

# Check Signature Size
echo "--- ✍️ Signature ---"
echo "This is a test message." > "$MESSAGE_FILE"
./openssl pkeyutl -sign -inkey "$PRIVATE_KEY_FILE" -in "$MESSAGE_FILE" -provider default -provider oqsprovider -out "$SIGNATURE_FILE" 2>/dev/null
# ./openssl dgst -sha256 -sign "$PRIVATE_KEY_FILE" -out "$SIGNATURE_FILE" "$MESSAGE_FILE" 2>/dev/null
sig_bytes=$(wc -c < "$SIGNATURE_FILE")
echo "Size: ${BOLD}$sig_bytes bytes${NORMAL}"
echo
