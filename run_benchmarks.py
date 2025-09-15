#!/usr/bin/env python3
import os
import sys

# Add the scripts-py directory to sys.path and import get_all_metrics
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts-py'))
from csv_builder import init_benchmarks_csv, add_benchmark_row  # type: ignore
from calculate_averages import calculate_averages, calculate_medians  # type: ignore

if __name__ == "__main__":

    # Set path for benchmarks file.
    out_csv = os.path.join(os.path.dirname(__file__), 'results', 'benchmarks.csv')

    # Create the CSV file
    init_benchmarks_csv(out_csv=out_csv)

    """ BENCHMARKING PROCESS BEGINS """
    print("\n\033[92mStarting benchmarking process...\033[0m")
    print("\n\033[93mBenchmarking RSA 2048...\033[0m")

    # Benchmark RSA
    prefix = 'rsa'
    avg_keypair, avg_csr, avg_cert, avg_verify = calculate_averages(prefix, runs=20)
    med_keypair, med_csr, med_cert, med_verify = calculate_medians(prefix, runs=20)

    # Add results to CSV
    """add_benchmark_row(out_csv, [
        'rsa',
        'RSA 2048',
        5,
        256,
        2048,
        256,
        *avg_keypair,
        *avg_csr,
        *avg_cert,
        *avg_verify,
        *med_keypair,
        *med_csr,
        *med_cert,
        *med_verify
    ])"""

    # Print to console
    print("\n\033[92mRSA 2048 Benchmarking Complete. See metrics below:\033[0m")
    print(f"RSA Average Keypair Metrics: {avg_keypair}")
    print(f"RSA Average CSR Metrics: {avg_csr}")
    print(f"RSA Average Cert Metrics: {avg_cert}")
    print(f"RSA Average Verify Metrics: {avg_verify}")
    print(f"RSA Median Keypair Metrics: {med_keypair}")
    print(f"RSA Median CSR Metrics: {med_csr}")
    print(f"RSA Median Cert Metrics: {med_cert}")
    print(f"RSA Median Verify Metrics: {med_verify}")
