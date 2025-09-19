#!/usr/bin/env python3
import os
import sys

# Add the scripts-py directory to sys.path and import get_all_metrics
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts-py'))
from csv_builder import init_benchmarks_csv, add_benchmarks  # type: ignore
from calculate_averages import calculate_averages, calculate_medians  # type: ignore

def run_benchmark(out_csv, prefix, static_items, runs=1):
    print(f"\n\033[93mBenchmarking {static_items[1]}...\033[0m")
    avg_kp, avg_csr, avg_cert, avg_ver = calculate_averages(prefix, runs=runs)
    med_kp, med_csr, med_cert, med_ver = calculate_medians(prefix, runs=runs)
    add_benchmarks(
        out_csv,
        static_items,
        [avg_kp, avg_csr, avg_cert, avg_ver],
        [med_kp, med_csr, med_cert, med_ver]
    )
    print(f"\n\033[92m{static_items[1]} Benchmarking Complete. See metrics below:\033[0m")
    print("Metrics Order: [CPU Cycles, Real time, CPU time, Memory/Peak RSS]")
    for label, avg, med in [
        ("Keypair", avg_kp, med_kp),
        ("CSR",     avg_csr, med_csr),
        ("Cert",    avg_cert, med_cert),
        ("Verify",  avg_ver, med_ver),
    ]:
        print(f"{static_items[1]} Average {label} Metrics: {avg}")
        print(f"{static_items[1]} Median  {label} Metrics: {med}")

if __name__ == "__main__":

    # Set path for benchmarks file.
    out_csv = os.path.join(os.path.dirname(__file__), 'results', 'benchmarks.csv')

    # Create the CSV file
    init_benchmarks_csv(out_csv=out_csv)

    """ BENCHMARKING PROCESS BEGINS """
    print("\n\033[92mStarting benchmarking process...\033[0m")

    # Run benchmarks for each algorithm
    # Arguments: (output_csv, prefix, [algorithm id, algorithm name, NIST security level, private key size, public key size, signature size])
    run_benchmark(out_csv, 'rsa',        ['rsa', 'RSA 2048', 'N/A','1191','294','256'])
    run_benchmark(out_csv, 'dilithium2', ['mldsa44','Dilithium 2', '2','2626','1334','2420'])
    run_benchmark(out_csv, 'dilithium3', ['mldsa65','Dilithium 3', '3','4098','1974','3309'])
    run_benchmark(out_csv, 'dilithium5', ['mldsa87','Dilithium 5', '5','4962','2614','4627'])
    run_benchmark(out_csv, 'sphincssha1s', ['slh-dsa-sha2-128s','SPHINCS+ SHA 128s', '1','84','50','7856'])
    run_benchmark(out_csv, 'sphincssha1f', ['slh-dsa-sha2-128f','SPHINCS+ SHA 128f', '1','84','50','17088'])
    run_benchmark(out_csv, 'sphincssha3s', ['slh-dsa-sha2-192s','SPHINCS+ SHA 192s', '3','116','66','16224'])
    run_benchmark(out_csv, 'sphincssha3f', ['slh-dsa-sha2-192f','SPHINCS+ SHA 192f', '3','116','66','35664'])
    run_benchmark(out_csv, 'sphincssha5s', ['slh-dsa-sha2-256s','SPHINCS+ SHA 256s', '5','150','82','29792'])
    run_benchmark(out_csv, 'sphincssha5f', ['slh-dsa-sha2-256f','SPHINCS+ SHA 256f', '5','150','82','49856'])
    run_benchmark(out_csv, 'sphincsshake1s', ['slh-dsa-shake-128s','SPHINCS+ SHAKE 128s', '1','84','50','7856'])
    run_benchmark(out_csv, 'sphincsshake1f', ['slh-dsa-shake-128f','SPHINCS+ SHAKE 128f', '1','84','50','17088'])
    run_benchmark(out_csv, 'sphincsshake3s', ['slh-dsa-shake-192s','SPHINCS+ SHAKE 192s', '3','116','66','16224'])
    run_benchmark(out_csv, 'sphincsshake3f', ['slh-dsa-shake-192f','SPHINCS+ SHAKE 192f', '3','116','66','35664'])
    run_benchmark(out_csv, 'sphincsshake5s', ['slh-dsa-shake-256s','SPHINCS+ SHAKE 256s', '5','150','82','29792'])
    run_benchmark(out_csv, 'sphincsshake5f', ['slh-dsa-shake-256f','SPHINCS+ SHAKE 256f', '5','150','82','49856'])
    run_benchmark(out_csv, 'falcon512', ['falcon512','Falcon 512','1','2202','915','657'])
    run_benchmark(out_csv, 'falcon1024', ['falcon1024','Falcon 1024','5','4122','1811','1267'])
