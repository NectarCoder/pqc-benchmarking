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
        "NIST Security Level",
        "Public Key Size",
        "Private Key Size",
        "Signature Size",
        "Avg CPU Cycles for Private/Public Keygen",
        "Avg CPU Cycles for CSR Generation",
        "Avg CPU Cycles for Certificate Generation",
        "Avg CPU Cycles for Certificate Verification",
        "Avg Real time for Private/Public Keygen",
        "Avg Real time for CSR Generation",
        "Avg Real time for Certificate Generation",
        "Avg Real time for Certificate Verification",
        "Avg CPU time for Private/Public Keygen",
        "Avg CPU time for CSR Generation",
        "Avg CPU time for Certificate Generation",
        "Avg CPU time for Certificate Verification",
        "Avg Peak RSS for Private/Public Keygen (Memory Usage)",
        "Avg Peak RSS for CSR Generation (Memory Usage)",
        "Avg Peak RSS for Certificate Generation (Memory Usage)",
        "Avg Peak RSS for Certificate Verification (Memory Usage)",
        "Median CPU Cycles for Private/Public Keygen",
        "Median CPU Cycles for CSR Generation",
        "Median CPU Cycles for Certificate Generation",
        "Median CPU Cycles for Certificate Verification",
        "Median Real time for Private/Public Keygen",
        "Median Real time for CSR Generation",
        "Median Real time for Certificate Generation",
        "Median Real time for Certificate Verification",
        "Median CPU time for Private/Public Keygen",
        "Median CPU time for CSR Generation",
        "Median CPU time for Certificate Generation",
        "Median CPU time for Certificate Verification",
        "Median Peak RSS for Private/Public Keygen (Memory Usage)",
        "Median Peak RSS for CSR Generation (Memory Usage)",
        "Median Peak RSS for Certificate Generation (Memory Usage)",
        "Median Peak RSS for Certificate Verification (Memory Usage)",
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
