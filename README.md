# PQC Round 2 Digital Signature Algorithm Benchmarking  

Performance benchmarks on the fourteen digital-signature algorithms submitted to *NIST's Post-Quantum Cryptography Round 2 — Additional Digital Signature Schemes* [^1]. This repo builds upon concepts from previous works [^3], [^4] and aims to provide a way to analyze the performance of these algorithms in the context of public key infrastructure (PKI).  

## Outline of Algorithms Benchmarked  

The following 14 Round 2 algorithms are benchmarked [^1]:  
<details>
<summary><strong>Expand List</strong></summary>

- CROSS
- FAEST
- HAWK
- LESS
- MAYO
- Mirath
- MQOM
- PERK
- QR-UOV
- RYDE
- SDitH
- SNOVA
- SQISign
- UOV

</details><br>  

In order to provide a comparative baseline, the current 3 standardized schemes [^2] are also benchmarked:  

- CRYSTALS-Dilithium (Now known as ML-DSA) (FIPS 204)
- Sphincs+ (Now known as SLH-DSA) (FIPS 205)
- FALCON (Now known as FN-DSA) (FIPS 206)

## Building & Benchmarking  

This project heavily utilizes OpenSSL, liboqs, and oqs-provider. Before running benchmarks, complete the following prerequisites. Note that at this time, the benchmarking scripts and following setup is designed for an Ubuntu (18-24) environment.  
It is expected you have `sudo` access on the system you are using.  

1. Install OpenSSL 3.5.2 SEPARATELY from the apt/system-wide OpenSSL  

```bash
# Browse to your preferred directory
cd ~/Downloads

# Download from the OpenSSL github repo (or if newer version is available, update the URL)
wget https://github.com/openssl/openssl/releases/download/openssl-3.5.2/openssl-3.5.2.tar.gz

# Extract the tarball and browse into the extracted directory
tar -xvzf openssl-3.5.2.tar.gz; cd openssl-3.5.2

# Setup OpenSSL build config (installing to /opt/openssl-3.5.2)
./config --prefix=/opt/openssl-3.5.2 --openssldir=/opt/openssl-3.5.2 shared

# Build and install OpenSSL
make -j$(nproc) && sudo make install

# Set /opt/openssl path via ldconfig - in order to expose the newer OpenSSL libs
/opt/openssl-3.5.2/bin/openssl version; sudo ldconfig

# Verify installation
/opt/openssl-3.5.2/bin/openssl version

```

---

##### References

[^1]: List of Round 2 Digital Signature Candidates: [Round 2 Additional Signatures](https://csrc.nist.gov/Projects/pqc-dig-sig/round-2-additional-signatures)  

[^2]: Current standardized PQC Signature Schemes: [NIST Releases First 3 Finalized Post-Quantum Encryption Standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)  

[^3]: M. Raavi, P. Chandramouli, S. Wuthier, X. Zhou, and S.-Y. Chang, "Performance Characterization of Post-Quantum Digital Certificates," 2021 International Conference on Computer Communications and Networks (ICCCN), Jul. 2021, doi: [https://doi.org/10.1109/icccn52240.2021.9522179](https://doi.org/10.1109/icccn52240.2021.9522179).  

[^4]: M. Raavi, Q. Khan, S. Wuthier, P. Chandramouli, Y. Balytskyi, and S.-Y. Chang, “Security and Performance Analyses of Post-Quantum Digital Signature Algorithms and Their TLS and PKI Integrations,” Cryptography, vol. 9, no. 2, p. 38, Jun. 2025, doi: [https://doi.org/10.3390/cryptography9020038](https://doi.org/10.3390/cryptography9020038).  
