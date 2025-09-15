#!/usr/bin/env python3
import os
import sys

# Add the scripts-py directory to sys.path and import get_all_metrics
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts-py'))
from csv_builder import init_benchmarks_csv  # type: ignore
from calculate_averages import calculate_averages  # type: ignore

if __name__ == "__main__":

    # Set path for benchmarks file.
    out_csv = os.path.join(os.path.dirname(__file__), 'benchmarks.csv')

    # Create the CSV file
    init_benchmarks_csv(out_csv=out_csv)

    """ BENCHMARKING PROCESS BEGINS """
    # Benchmark RSA
    prefix = 'rsa'
    avg_keypair_metrics, avg_csr_metrics, avg_cert_metrics, avg_verify_metrics = calculate_averages(prefix)

    # Print to console
    print(f"RSA Average Keypair Metrics: {avg_keypair_metrics}")
    print(f"RSA Average CSR Metrics: {avg_csr_metrics}")
    print(f"RSA Average Cert Metrics: {avg_cert_metrics}")
    print(f"RSA Average Verify Metrics: {avg_verify_metrics}")
    