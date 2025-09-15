#!/usr/bin/env python3
import os
import sys

# Add the scripts-py directory to sys.path and import get_all_metrics
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts-py'))
from csv_builder import init_benchmarks_csv, add_benchmarks  # type: ignore
from calculate_averages import calculate_averages, calculate_medians  # type: ignore

if __name__ == "__main__":

    # Set path for benchmarks file.
    out_csv = os.path.join(os.path.dirname(__file__), 'results', 'benchmarks.csv')

    # Create the CSV file
    init_benchmarks_csv(out_csv=out_csv)

    """ BENCHMARKING PROCESS BEGINS """
    print("\n\033[92mStarting benchmarking process...\033[0m")

    # Benchmark RSA
    print("\n\033[93mBenchmarking RSA 2048...\033[0m")

    prefix = 'rsa'
    avg_keypair, avg_csr, avg_cert, avg_verify = calculate_averages(prefix, runs=20)
    med_keypair, med_csr, med_cert, med_verify = calculate_medians(prefix, runs=20)

    # First list static metadata, then avg metrics and med metrics grouped by metric type
    static_items = ['rsa', 'RSA 2048', 'todo', 'todo', 'todo', 'todo']
    avg_items = [avg_keypair, avg_csr, avg_cert, avg_verify]
    med_items = [med_keypair, med_csr, med_cert, med_verify]

    # Add results to CSV in a new row
    add_benchmarks(out_csv, static_items, avg_items, med_items)
    
    # Print to console
    print("\n\033[92mRSA 2048 Benchmarking Complete. See metrics below:\033[0m")
    print(f"Metrics Order: [CPU Cycles, Real time, CPU time, Memory/Peak RSS]")
    print(f"RSA Average Keypair Metrics: {avg_keypair}")
    print(f"RSA Average CSR Metrics: {avg_csr}")
    print(f"RSA Average Cert Metrics: {avg_cert}")
    print(f"RSA Average Verify Metrics: {avg_verify}")
    print(f"RSA Median Keypair Metrics: {med_keypair}")
    print(f"RSA Median CSR Metrics: {med_csr}")
    print(f"RSA Median Cert Metrics: {med_cert}")
    print(f"RSA Median Verify Metrics: {med_verify}")

    # Benchmark Dilithium2
    print("\n\033[93mBenchmarking Dilithium2...\033[0m")

    prefix = 'dilithium2'
    avg_keypair, avg_csr, avg_cert, avg_verify = calculate_averages(prefix, runs=20)
    med_keypair, med_csr, med_cert, med_verify = calculate_medians(prefix, runs=20)

    # First list static metadata, then avg metrics and med metrics grouped by metric type
    static_items = ['p256_mldsa44', 'Dilithium2', 'todo', 'todo', 'todo', 'todo',]
    avg_items = [avg_keypair, avg_csr, avg_cert, avg_verify]
    med_items = [med_keypair, med_csr, med_cert, med_verify]

    # Add results to CSV in a new row
    add_benchmarks(out_csv, static_items, avg_items, med_items)
    
    # Print to console
    print("\n\033[92mDilithium2 Benchmarking Complete. See metrics below:\033[0m")
    print(f"Metrics Order: [CPU Cycles, Real time, CPU time, Memory/Peak RSS]")
    print(f"Dilithium2 Average Keypair Metrics: {avg_keypair}")
    print(f"Dilithium2 Average CSR Metrics: {avg_csr}")
    print(f"Dilithium2 Average Cert Metrics: {avg_cert}")
    print(f"Dilithium2 Average Verify Metrics: {avg_verify}")
    print(f"Dilithium2 Median Keypair Metrics: {med_keypair}")
    print(f"Dilithium2 Median CSR Metrics: {med_csr}")
    print(f"Dilithium2 Median Cert Metrics: {med_cert}")
    print(f"Dilithium2 Median Verify Metrics: {med_verify}")

    # Benchmark Dilithium3
    print("\n\033[93mBenchmarking Dilithium3...\033[0m")

    prefix = 'dilithium3'
    avg_keypair, avg_csr, avg_cert, avg_verify = calculate_averages(prefix, runs=20)
    med_keypair, med_csr, med_cert, med_verify = calculate_medians(prefix, runs=20)

    # First list static metadata, then avg metrics and med metrics grouped by metric type
    static_items = ['p384_mldsa65', 'Dilithium3', 'todo', 'todo', 'todo', 'todo',]
    avg_items = [avg_keypair, avg_csr, avg_cert, avg_verify]
    med_items = [med_keypair, med_csr, med_cert, med_verify]

    # Add results to CSV in a new row
    add_benchmarks(out_csv, static_items, avg_items, med_items)
    
    # Print to console
    print("\n\033[92mDilithium3 Benchmarking Complete. See metrics below:\033[0m")
    print(f"Metrics Order: [CPU Cycles, Real time, CPU time, Memory/Peak RSS]")
    print(f"Dilithium3 Average Keypair Metrics: {avg_keypair}")
    print(f"Dilithium3 Average CSR Metrics: {avg_csr}")
    print(f"Dilithium3 Average Cert Metrics: {avg_cert}")
    print(f"Dilithium3 Average Verify Metrics: {avg_verify}")
    print(f"Dilithium3 Median Keypair Metrics: {med_keypair}")
    print(f"Dilithium3 Median CSR Metrics: {med_csr}")
    print(f"Dilithium3 Median Cert Metrics: {med_cert}")
    print(f"Dilithium3 Median Verify Metrics: {med_verify}")

    # Benchmark Dilithium5
    print("\n\033[93mBenchmarking Dilithium5...\033[0m")

    prefix = 'dilithium5'
    avg_keypair, avg_csr, avg_cert, avg_verify = calculate_averages(prefix, runs=20)
    med_keypair, med_csr, med_cert, med_verify = calculate_medians(prefix, runs=20)

    # First list static metadata, then avg metrics and med metrics grouped by metric type
    static_items = ['p384_mldsa65', 'Dilithium5', 'todo', 'todo', 'todo', 'todo',]
    avg_items = [avg_keypair, avg_csr, avg_cert, avg_verify]
    med_items = [med_keypair, med_csr, med_cert, med_verify]

    # Add results to CSV in a new row
    add_benchmarks(out_csv, static_items, avg_items, med_items)
    
    # Print to console
    print("\n\033[92mDilithium5 Benchmarking Complete. See metrics below:\033[0m")
    print(f"Metrics Order: [CPU Cycles, Real time, CPU time, Memory/Peak RSS]")
    print(f"Dilithium5 Average Keypair Metrics: {avg_keypair}")
    print(f"Dilithium5 Average CSR Metrics: {avg_csr}")
    print(f"Dilithium5 Average Cert Metrics: {avg_cert}")
    print(f"Dilithium5 Average Verify Metrics: {avg_verify}")
    print(f"Dilithium5 Median Keypair Metrics: {med_keypair}")
    print(f"Dilithium5 Median CSR Metrics: {med_csr}")
    print(f"Dilithium5 Median Cert Metrics: {med_cert}")
    print(f"Dilithium5 Median Verify Metrics: {med_verify}")
