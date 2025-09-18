#!/usr/bin/env python3

import csv
import os


def init_benchmarks_csv(out_csv=None):
    """
    Initialize/overwrite the benchmarks.csv file with the required header.
    """

    # Define the CSV column names
    header = [
        "Algorithm ID",
        "Algorithm Name",
        "Security Level",
        "Private Key Size (bytes)",
        "Public Key Size (bytes)",
        "Signature Size (bytes)",
        # Average cycles (no unit)
        "Avg Cycles Keygen",
        "Avg Cycles CSR",
        "Avg Cycles CertGen",
        "Avg Cycles CertVerify",
        # Average real time (ms)
        "Avg Real Time (ms) Keygen",
        "Avg Real Time (ms) CSR",
        "Avg Real Time (ms) CertGen",
        "Avg Real Time (ms) CertVerify",
        # Average CPU time (ms)
        "Avg CPU Time (ms) Keygen",
        "Avg CPU Time (ms) CSR",
        "Avg CPU Time (ms) CertGen",
        "Avg CPU Time (ms) CertVerify",
        # Average memory (KB)
        "Avg Peak RSS (KB) Keygen",
        "Avg Peak RSS (KB) CSR",
        "Avg Peak RSS (KB) CertGen",
        "Avg Peak RSS (KB) CertVerify",
        # Median cycles (no unit)
        "Med Cycles Keygen",
        "Med Cycles CSR",
        "Med Cycles CertGen",
        "Med Cycles CertVerify",
        # Median real time (ms)
        "Med Real Time (ms) Keygen",
        "Med Real Time (ms) CSR",
        "Med Real Time (ms) CertGen",
        "Med Real Time (ms) CertVerify",
        # Median CPU time (ms)
        "Med CPU Time (ms) Keygen",
        "Med CPU Time (ms) CSR",
        "Med CPU Time (ms) CertGen",
        "Med CPU Time (ms) CertVerify",
        # Median memory (KB)
        "Med Peak RSS (KB) Keygen",
        "Med Peak RSS (KB) CSR",
        "Med Peak RSS (KB) CertGen",
        "Med Peak RSS (KB) CertVerify",
    ]

    # Ensure the parent directory exists
    base_dir = os.path.dirname(out_csv)
    if base_dir and not os.path.exists(base_dir):
        os.makedirs(base_dir, exist_ok=True)

    # If benchmarks.csv exists, rename it to benchmarks_old.csv or benchmarks_old_N.csv
    if os.path.exists(out_csv):
        old_csv = os.path.join(base_dir, "benchmarks_old.csv")
        if not os.path.exists(old_csv):
            os.rename(out_csv, old_csv)
        else:
            i = 1
            while True:
                numbered_old_csv = os.path.join(base_dir, f"benchmarks_old_{i}.csv")
                if not os.path.exists(numbered_old_csv):
                    os.rename(out_csv, numbered_old_csv)
                    break
                i += 1

    # Write the header to benchmarks.csv
    with open(out_csv, "w", newline="") as f:
        csv.writer(f).writerow(header)

def add_benchmarks(out_csv, static_items, avg_items, med_items):
    """
    Add the metrics to the CSV file as a new row.
    """
    def insert_row(out_csv, row_items):
        """
        Insert a row into the specified CSV file.
        """
        # Ensure the CSV file exists
        if not os.path.exists(out_csv):
            raise FileNotFoundError(f"CSV file {out_csv} does not exist.")
        # Append the new row
        with open(out_csv, "a", newline="") as f:
            csv.writer(f).writerow(row_items)
    
    # Each metrics list: [cycles, real, cpu_time, memory]
    avg_flat = []
    for i in range(4):  # 0: cycles, 1: real, 2: cpu_time, 3: memory
        for grp in avg_items:
            avg_flat.append(grp[i])
    med_flat = []
    for i in range(4):  # same order for medians
        for grp in med_items:
            med_flat.append(grp[i])
    row = static_items + avg_flat + med_flat
    insert_row(out_csv, row)
