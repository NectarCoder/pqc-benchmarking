#!/usr/bin/env python3
import os
import sys

# Add the scripts-py directory to sys.path and import get_all_metrics
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts-py'))
from csv_builder import init_benchmarks_csv, add_benchmarks  # type: ignore
from calculate_averages import calculate_averages, calculate_medians  # type: ignore

def run_benchmark(out_csv, prefix, static_items, runs=5):
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
    run_benchmark(out_csv, 'rsa',        ['rsa',        'RSA 2048',    'N/A','1704','451','2048'])
    run_benchmark(out_csv, 'dilithium2', ['p256_mldsa44','Dilithium2', '2','5502','1950','2420'])
    run_benchmark(out_csv, 'dilithium3', ['p384_mldsa65','Dilithium3', '3','8423','2860','3309'])
    run_benchmark(out_csv, 'dilithium5', ['p384_mldsa65','Dilithium5', '5','10536','3774','4627'])
