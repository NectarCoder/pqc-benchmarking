#!/usr/bin/env python3

import csv
import os

"""
Initialize/overwrite the benchmarks.csv file with the required header.
"""
def init_benchmarks_csv(out_csv=None):
    
    # Define the CSV column names
    header = [
        'Algorithm ID',
        'Algorithm Name',
        'NIST Security Level',
        'Public Key Size',
        'Private Key Size',
        'Signature Size',
        'Avg CPU time for Private/Public Keygen',
        'Avg CPU time for CSR Generation',
        'Avg CPU time for Certificate Generation',
        'Avg CPU time for Certificate Verification',
        'Avg Real time for Private/Public Keygen',
        'Avg Real time for CSR Generation',
        'Avg Real time for Certificate Generation',
        'Avg Real time for Certificate Verification',
        'Median CPU time for Private/Public Keygen',
        'Median CPU time for CSR Generation',
        'Median CPU time for Certificate Generation',
        'Median CPU time for Certificate Verification',
        'Median Real time for Private/Public Keygen',
        'Median Real time for CSR Generation',
        'Median Real time for Certificate Generation',
        'Median Real time for Certificate Verification',
        'Avg CPU Cycles for Private/Public Keygen',
        'Avg CPU Cycles for CSR Generation',
        'Avg CPU Cycles for Certificate Generation',
        'Avg CPU Cycles for Certificate Verification',
        'Median CPU Cycles for Private/Public Keygen',
        'Median CPU Cycles for CSR Generation',
        'Median CPU Cycles for Certificate Generation',
        'Median CPU Cycles for Certificate Verification',
        'Avg Peak RSS for Private/Public Keygen (Memory Usage)',
        'Avg Peak RSS for CSR Generation (Memory Usage)',
        'Avg Peak RSS for Certificate Generation (Memory Usage)',
        'Avg Peak RSS for Certificate Verification (Memory Usage)',
        'Median Peak RSS for Private/Public Keygen (Memory Usage)',
        'Median Peak RSS for CSR Generation (Memory Usage)',
        'Median Peak RSS for Certificate Generation (Memory Usage)',
        'Median Peak RSS for Certificate Verification (Memory Usage)'
    ]

    # If benchmarks.csv exists, rename it to benchmarks_old.csv or benchmarks_old_N.csv
    if os.path.exists(out_csv):
        base_dir = os.path.dirname(out_csv)
        old_csv = os.path.join(base_dir, 'benchmarks_old.csv')
        if not os.path.exists(old_csv):
            os.rename(out_csv, old_csv)
        else:
            i = 1
            while True:
                numbered_old_csv = os.path.join(base_dir, f'benchmarks_old_{i}.csv')
                if not os.path.exists(numbered_old_csv):
                    os.rename(out_csv, numbered_old_csv)
                    break
                i += 1

    # Write the header to benchmarks.csv
    with open(out_csv, 'w', newline='') as f:
        csv.writer(f).writerow(header)
