#!/bin/bash

# List of algorithms to check
algorithms=(
    "falcon512"
    "falcon1024"
    "mayo1"
    "mayo2"
    "mayo3"
    "mayo5"
    "CROSSrsdp128small"
    "CROSSrsdp192small"
    "CROSSrsdp256small"
    "CROSSrsdpg128small"
    "CROSSrsdpg192small"
    "CROSSrsdpg256small"
    "snova2454"
    "snova37172"
    "snova2583"
    "snova56252"
    "snova49113"
    "snova3784"
    "snova2455"
    "snova60104"
    "snova2965"
    "snova66153"
    "snova75332"
    "OV_Is"
    "OV_Ip"
    "OV_III"
    "OV_V"
    "hawk512"
    "hawk1024"
    "faest128s"
    "faest192s"
    "faest256s"
    "faestem128s"
    "faestem192s"
    "faestem256s"
    "perkak1short"
    "perkak3short"
    "perkak5short"
    "ryde1s"
    "ryde3s"
    "ryde5s"
    "mirathtcith1ashort"
    "mirathtcith1bshort"
    "mirathtcith3ashort"
    "mirathtcith3bshort"
    "mirathtcith5ashort"
    "mirathtcith5bshort"
    "sdithcat1short"
    "sdithcat3short"
    "sdithcat5short"
    "mqom2cat1gf2shortr3"
    "mqom2cat1gf2shortr5"
    "mqom2cat1gf16shortr3"
    "mqom2cat1gf16shortr5"
    "mqom2cat1gf256shortr3"
    "mqom2cat1gf256shortr5"
    "mqom2cat3gf2shortr3"
    "mqom2cat3gf2shortr5"
    "mqom2cat3gf16shortr3"
    "mqom2cat3gf16shortr5"
    "mqom2cat3gf256shortr3"
    "mqom2cat3gf256shortr5"
    "mqom2cat5gf2shortr3"
    "mqom2cat5gf2shortr5"
    "mqom2cat5gf16shortr3"
    "mqom2cat5gf16shortr5"
    "mqom2cat5gf256shortr3"
    "mqom2cat5gf256shortr5"
    "less252192"
    "less25268"
    "less25245"
    "less400220"
    "less400102"
    "less548345"
    "less548137"
    "qruov1q127L3v156m54"
    "qruov1q7L10v740m100"
    "qruov1q31L3v165m60"
    "qruov1q31L10v600m70"
    "qruov3q127L3v228m78"
    "qruov3q7L10v1100m140"
    "qruov3q31L3v246m87"
    "qruov3q31L10v890m100"
    "qruov5q127L3v306m105"
    "qruov5q7L10v1490m190"
    "qruov5q31L3v324m114"
    "qruov5q31L10v1120m120"
)

# Arrays to hold results
unique_private_algorithms=()
same_private_algorithms=()
unique_public_algorithms=()
same_public_algorithms=()

for alg in "${algorithms[@]}"; do
    echo "Checking algorithm: $alg"
    
    # Generate 10 private keys and extract public keys
    private_hashes=()
    public_hashes=()
    for i in {1..10}; do
        ./openssl genpkey -algorithm "$alg" -out "private$i.key" -provider default -provider oqsprovider
        if [ $? -ne 0 ]; then
            echo "Error generating private key for $alg, skipping."
            continue 2
        fi
        ./openssl pkey -in "private$i.key" -pubout -out "public$i.key" -provider default -provider oqsprovider
        if [ $? -ne 0 ]; then
            echo "Error extracting public key for $alg, skipping."
            continue 2
        fi
        private_hash=$(md5sum "private$i.key" | awk '{print $1}')
        public_hash=$(md5sum "public$i.key" | awk '{print $1}')
        private_hashes+=("$private_hash")
        public_hashes+=("$public_hash")
    done
    
    # Check if all private hashes are the same
    first_private_hash="${private_hashes[0]}"
    private_all_same=true
    for hash in "${private_hashes[@]}"; do
        if [ "$hash" != "$first_private_hash" ]; then
            private_all_same=false
            break
        fi
    done
    
    # Check if all public hashes are the same
    first_public_hash="${public_hashes[0]}"
    public_all_same=true
    for hash in "${public_hashes[@]}"; do
        if [ "$hash" != "$first_public_hash" ]; then
            public_all_same=false
            break
        fi
    done
    
    if $private_all_same; then
        same_private_algorithms+=("$alg")
    else
        unique_private_algorithms+=("$alg")
    fi
    
    if $public_all_same; then
        same_public_algorithms+=("$alg")
    else
        unique_public_algorithms+=("$alg")
    fi
    
    # Clean up keys for this algorithm
    rm -f private*.key public*.key
done

# Print summary
echo ""
echo "Summary for Private Keys:"
echo "Algorithms with unique private keys each generation (good):"
for alg in "${unique_private_algorithms[@]}"; do
    echo "  - $alg"
done

echo ""
echo "Algorithms with the same private key each generation (bad):"
for alg in "${same_private_algorithms[@]}"; do
    echo "  - $alg"
done

echo ""
echo "Summary for Public Keys:"
echo "Algorithms with unique public keys each generation (good):"
for alg in "${unique_public_algorithms[@]}"; do
    echo "  - $alg"
done

echo ""
echo "Algorithms with the same public key each generation (bad):"
for alg in "${same_public_algorithms[@]}"; do
    echo "  - $alg"
done

# Final cleanup in case of errors
rm -f private*.key public*.key