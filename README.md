# PQC Round 2 Digital Signature Algorithm Benchmarking  

Performance benchmarks on the fourteen digital-signature algorithms submitted to *NIST's Post-Quantum Cryptography Round 2 — Additional Digital Signature Schemes* [^1]. This repo builds upon concepts from previous works [^3], [^4] and aims to provide a way to analyze the performance of these algorithms in the context of public key infrastructure (PKI).  

## Project Context: Algorithm & Metrics

### List of Algorithms

The following 14 Round 2 algorithms are benchmarked [^1]:  

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

In order to provide a comparative baseline, the current 3 standardized schemes [^2] are also benchmarked:  

- CRYSTALS-Dilithium (Now known as ML-DSA) (FIPS 204)
- Sphincs+ (Now known as SLH-DSA) (FIPS 205)
- FALCON (Now known as FN-DSA) (FIPS 206)

### What are the benchmarks?  

The benchmarks focus on measuring the performance of each algorithm in terms of key generation, request, signing, and verification times.  
For each metric, we respectively note the algorithm version and the NIST security level (1, 2, 3, 4, 5) [^5].
In general, the objective is to find:  

- Time taken to:
    - Generate a private & public key pair
    - Extract public key from the private key
    - Generate Certificate Signing Request (CSR)
    - Sign the CSR and generate a self-signed certificate
    - Verify the self-signed certificate (in milliseconds)
- CPU cycles taken to:
    - Generate a private & public key pair
    - Extract public key from the private key
    - Generate Certificate Signing Request (CSR)
    - Sign the CSR and generate a self-signed certificate
    - Verify the self-signed certificate (in CPU cycles)
- Memory consumption during:
    - Key pair generation
    - CSR generation
    - Certificate signing
    - Certificate verification (in KB)
- File sizes of:
    - Private key
    - Public key
    - CSR
    - Self-signed certificate (in bytes)

More technically, we define the metrics listed below:  

<details>
<summary>Click to expand: Full List of Metrics</summary>

- **User & kernel time** *(total CPU time, in milliseconds)* for <u>generating the private key</u>
- **User & kernel time** *(total CPU time, in milliseconds)* for <u>extracting the public key from the private key</u>
- **User & kernel time** *(total CPU time, in milliseconds)* for <u>generating the CSR</u>
- **User & kernel time** *(total CPU time, in milliseconds)* for <u>signing CSR & generate a self-signed certificate</u>
- **User & kernel time** *(total CPU time, in milliseconds)* for <u>verifying the self-signed certificate</u>
- **User & kernel time** *(total CPU time, in milliseconds)* for <u>generating key pair (generating private key + extracting public key)</u>
- **User & kernel time** *(total CPU time, in milliseconds)* for <u>ALL operations combined</u>
- **Real time** *(wall-clock time, in milliseconds)* for <u>generating the private key</u>
- **Real time** *(wall-clock time, in milliseconds)* for <u>extracting the public key from the private key</u>
- **Real time** *(wall-clock time, in milliseconds)* for <u>generating the CSR</u>
- **Real time** *(wall-clock time, in milliseconds)* for <u>signing CSR & generating a self-signed certificate</u>
- **Real time** *(wall-clock time, in milliseconds)* for <u>verifying the self-signed certificate</u>
- **Real time** *(wall-clock time, in milliseconds)* for <u>generating key pair (generating private key + extracting public key)</u>
- **Real time** *(wall-clock time, in milliseconds)* for <u>ALL operations combined</u>
- **CPU Cycles** for <u>generating the private key</u>
- **CPU Cycles** for <u>extracting the public key from the private key</u>
- **CPU Cycles** for <u>generating the CSR</u>
- **CPU Cycles** for <u>signing CSR & generating a self-signed certificate</u>
- **CPU Cycles** for <u>verifying the self-signed certificate</u>
- **CPU Cycles** for <u>generating key pair (generating private key + extracting public key)</u>
- **CPU Cycles** for <u>ALL operations combined</u>
- **Maximum memory usage/Peak RSS (Resident Settings Size)** *(in KB)* for <u>generating the private key</u>
- **Maximum memory usage/Peak RSS (Resident Settings Size)** *(in KB)* for <u>extracting the public key from the private key</u>
- **Maximum memory usage/Peak RSS (Resident Settings Size)** *(in KB)* for <u>generating the CSR</u>
- **Maximum memory usage/Peak RSS (Resident Settings Size)** *(in KB)* for <u>signing CSR & generating a self-signed certificate</u>
- **Maximum memory usage/Peak RSS (Resident Settings Size)** *(in KB)* for <u>verifying the self-signed certificate</u>
- **Maximum memory usage/Peak RSS (Resident Settings Size)** *(in KB)* for <u>generating key pair (generating private key + extracting public key)</u>
- **Maximum memory usage/Peak RSS (Resident Settings Size)** *(in KB)* for <u>ALL operations combined</u>
- **File size** *(in bytes)* of the <u>private key</u>
- **File size** *(in bytes)* of the <u>public key</u>
- **File size** *(in bytes)* of the <u>CSR</u>
- **File size** *(in bytes)* of the <u>self-signed certificate</u>  

</details>

Based on these metrics, the actual benchmarks are calculated ***(over 1000 attempts for each algorithm)***:

<details>
<summary>Click to expand: Full List of Benchmarks</summary>

- **Average CPU time** for <u>generating the private key</u>
- **Average CPU time** for <u>extracting the public key from the private key</u>
- **Average CPU time** for <u>generating the CSR</u>
- **Average CPU time** for <u>signing CSR & generating a self-signed certificate</u>
- **Average CPU time** for <u>verifying the self-signed certificate</u>
- **Average CPU time** for <u>generating key pair (generating private key + extracting public key)</u>
- **Average CPU time** for <u>ALL operations combined</u>
- **Average wall-clock time** for <u>generating the private key</u>
- **Average wall-clock time** for <u>extracting the public key from the private key</u>
- **Average wall-clock time** for <u>generating the CSR</u>
- **Average wall-clock time** for <u>signing CSR & generating a self-signed certificate</u>
- **Average wall-clock time** for <u>verifying the self-signed certificate</u>
- **Average wall-clock time** for <u>generating key pair (generating private key + extracting public key)</u>
- **Average wall-clock time** for <u>ALL operations combined</u>
- **Median CPU time** for <u>generating the private key</u>
- **Median CPU time** for <u>extracting the public key from the private key</u>
- **Median CPU time** for <u>generating the CSR</u>
- **Median CPU time** for <u>signing CSR & generating a self-signed certificate</u>
- **Median CPU time** for <u>verifying the self-signed certificate</u>
- **Median CPU time** for <u>generating key pair (generating private key + extracting public key)</u>
- **Median CPU time** for <u>ALL operations combined</u>
- **Median wall-clock time** for <u>generating the private key</u>
- **Median wall-clock time** for <u>extracting the public key from the private key</u>
- **Median wall-clock time** for <u>generating the CSR</u>
- **Median wall-clock time** for <u>signing CSR & generating a self-signed certificate</u>
- **Median wall-clock time** for <u>verifying the self-signed certificate</u>
- **Median wall-clock time** for <u>generating key pair (generating private key + extracting public key)</u>
- **Median wall-clock time** for <u>ALL operations combined</u>
- **Average CPU Cycles** for <u>generating the private key</u>
- **Average CPU Cycles** for <u>extracting the public key from the private key</u>
- **Average CPU Cycles** for <u>generating the CSR</u>
- **Average CPU Cycles** for <u>signing CSR & generating a self-signed certificate</u>
- **Average CPU Cycles** for <u>verifying the self-signed certificate</u>
- **Average CPU Cycles** for <u>generating key pair (generating private key + extracting public key)</u>
- **Average CPU Cycles** for <u>ALL operations combined</u>
- **Median CPU Cycles** for <u>generating the private key</u>
- **Median CPU Cycles** for <u>extracting the public key from the private key</u>
- **Median CPU Cycles** for <u>generating the CSR</u>
- **Median CPU Cycles** for <u>signing CSR & generating a self-signed certificate</u>
- **Median CPU Cycles** for <u>verifying the self-signed certificate</u>
- **Median CPU Cycles** for <u>generating key pair (generating private key + extracting public key)</u>
- **Median CPU Cycles** for <u>ALL operations combined</u>
- **Average Peak RSS** for <u>generating the private key</u>
- **Average Peak RSS** for <u>extracting the public key from the private key</u>
- **Average Peak RSS** for <u>generating the CSR</u>
- **Average Peak RSS** for <u>signing CSR & generating a self-signed certificate</u>
- **Average Peak RSS** for <u>verifying the self-signed certificate</u>
- **Average Peak RSS** for <u>generating key pair (generating private key + extracting public key)</u>
- **Average Peak RSS** for <u>ALL operations combined</u>
- **Median Peak RSS** for <u>generating the private key</u>
- **Median Peak RSS** for <u>extracting the public key from the private key</u>
- **Median Peak RSS** for <u>generating the CSR</u>
- **Median Peak RSS** for <u>signing CSR & generating a self-signed certificate</u>
- **Median Peak RSS** for <u>verifying the self-signed certificate</u>
- **Median Peak RSS** for <u>generating key pair (generating private key + extracting public key)</u>
- **Median Peak RSS** for <u>ALL operations combined</u>
- **Average file size** of the <u>private key</u>
- **Average file size** of the <u>public key</u>
- **Average file size** of the <u>CSR</u>
- **Average file size** of the <u>self-signed certificate</u>

</details>

## Building & Benchmarking

### Prerequisites

This project uses OpenSSL, liboqs, and oqs-provider; these must be setup before running benchmarks.  
**The following instructions are designed for an <u>Ubuntu (22-24)</u> environment.**  

1. Setup Dependencies  
From the project root, run [scripts/install_dependencies.sh](/scripts/install_dependencies.sh):  

```bash
./scripts/install_dependencies.sh
```

2. Set perf permissions
To able to count CPU cycles, the system perf paranoia level needs to be set to 1 or lower.  
From the project root, run [scripts/set_perf_level.sh](/scripts/set_perf_level.sh) (This will set the level to 1): 

```bash
./scripts/set_perf_level.sh
```

Since this is a general security risk, you may want to revert this change after benchmarking.  
Run the following command to revert:  

```bash
./scripts/reset_perf_level.sh
```

3. Setup OpenSSL with OQS-Provider and liboqs
From the project root, run [scripts/install_pqc_openssl.sh](/scripts/install_pqc_openssl.sh):

```bash
./scripts/install_pqc_openssl.sh
```

### Benchmarking

**TODO**

---

##### References & Notes

[^1]: List of Round 2 Digital Signature Candidates: [Round 2 Additional Signatures](https://csrc.nist.gov/Projects/pqc-dig-sig/round-2-additional-signatures)  

[^2]: Current standardized PQC Signature Schemes: [NIST Releases First 3 Finalized Post-Quantum Encryption Standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)  

[^3]: M. Raavi, P. Chandramouli, S. Wuthier, X. Zhou, and S.-Y. Chang, "Performance Characterization of Post-Quantum Digital Certificates," 2021 International Conference on Computer Communications and Networks (ICCCN), Jul. 2021, doi: [https://doi.org/10.1109/icccn52240.2021.9522179](https://doi.org/10.1109/icccn52240.2021.9522179).  

[^4]: M. Raavi, Q. Khan, S. Wuthier, P. Chandramouli, Y. Balytskyi, and S.-Y. Chang, “Security and Performance Analyses of Post-Quantum Digital Signature Algorithms and Their TLS and PKI Integrations,” Cryptography, vol. 9, no. 2, p. 38, Jun. 2025, doi: [https://doi.org/10.3390/cryptography9020038](https://doi.org/10.3390/cryptography9020038).  

[^5]: By algorithm version, we mean the specific level of the algorithm, e.g. for Dilithium (which is one algorithm): p256_mldsa44 (level 2), p384_mldsa65 (level 3), & p521_mldsa87 (level 5) - each with different security levels. Also see: NIST Security Levels: [PQC Security (Evaluation Criteria)](https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization/evaluation-criteria/security-(evaluation-criteria))