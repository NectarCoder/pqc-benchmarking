#!/usr/bin/env python3
import os
import sys
import csv

"""
Setup the benchmarks.csv file with the required header.
"""
def init_benchmarks_csv():
    """Create or overwrite benchmarks.csv with the required header."""
    out_csv = os.path.join(os.path.dirname(__file__), 'benchmarks.csv')
    
    header = [
        'Algorithm ID',
        'Algorithm Name',
        'NIST Security Level',
        'Public Key Size',
        'Private Key Size',
        'Signature Size',
        'Avg CPU time for Private Keygen',
        'Avg CPU time for Public Keygen',
        'Avg CPU time for CSR generation',
        'Avg CPU time for Certificate generation',
        'Avg CPU time for Private/Public Keypair generation',
        'Avg CPU time for All Operations',
        'Avg Real time for Private Keygen',
        'Avg Real time for Public Keygen',
        'Avg Real time for CSR generation',
        'Avg Real time for Certificate generation',
        'Avg Real time for Private/Public Keypair generation',
        'Avg Real time for All Operations',
        'Median CPU time for Private Keygen',
        'Median CPU time for Public Keygen',
        'Median CPU time for CSR generation',
        'Median CPU time for Certificate generation',
        'Median CPU time for Private/Public Keypair generation',
        'Median CPU time for All Operations',
        'Median Real time for Private Keygen',
        'Median Real time for Public Keygen',
        'Median Real time for CSR generation',
        'Median Real time for Certificate generation',
        'Median Real time for Private/Public Keypair generation',
        'Median Real time for All Operations',
        'Avg CPU Cycles for Private Keygen',
        'Avg CPU Cycles for Public Keygen',
        'Avg CPU Cycles for CSR generation',
        'Avg CPU Cycles for Certificate generation',
        'Avg CPU Cycles for Private/Public Keypair generation',
        'Avg CPU Cycles for All Operations',
        'Median CPU Cycles for Private Keygen',
        'Median CPU Cycles for Public Keygen',
        'Median CPU Cycles for CSR generation',
        'Median CPU Cycles for Certificate generation',
        'Median CPU Cycles for Private/Public Keypair generation',
        'Median CPU Cycles for All Operations',
        'Avg Peak RSS for Private Keygen (Memory Usage)',
        'Avg Peak RSS for Public Keygen (Memory Usage)',
        'Avg Peak RSS for CSR generation (Memory Usage)',
        'Avg Peak RSS for Certificate generation (Memory Usage)',
        'Avg Peak RSS for Private/Public Keypair generation (Memory Usage)',
        'Avg Peak RSS for All Operations (Memory Usage)',
        'Median Peak RSS for Private Keygen (Memory Usage)',
        'Median Peak RSS for Public Keygen (Memory Usage)',
        'Median Peak RSS for CSR generation (Memory Usage)',
        'Median Peak RSS for Certificate generation (Memory Usage)',
        'Median Peak RSS for Private/Public Keypair generation (Memory Usage)',
        'Median Peak RSS for All Operations (Memory Usage)'
    ]
    # Always write (overwrite) header for a clean start
    with open(out_csv, 'w', newline='') as f:
        csv.writer(f).writerow(header)

# Add the scripts-py directory to sys.path and import get_all_metrics
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts-py'))
from extract_timing_metrics import get_all_metrics  # type: ignore

if __name__ == "__main__":

    # Initialize the CSV with the correct header
    init_benchmarks_csv()

    # TODO: complete calculate_averages.py and call it here to append averages to benchmarks.csv
    prefix = 'rsa'
    cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics = get_all_metrics(prefix)
    print("cert:", cert_metrics)
    print("csr:", csr_metrics)
    print("private:", private_metrics)
    print("public:", public_metrics)
    print("verify:", verify_metrics)
