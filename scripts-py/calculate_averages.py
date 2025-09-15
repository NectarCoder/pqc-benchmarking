#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts-py'))
from extract_timing_metrics import get_all_metrics  # type: ignore

def calculate_averages(prefix):

    # Initialize metrics
    # Note: order is [cpu_cycles, real_time, cpu_time]
    avg_keypair_metrics = [0.0, 0.0, 0.0]
    avg_csr_metrics = [0.0, 0.0, 0.0]
    avg_cert_metrics = [0.0, 0.0, 0.0]
    avg_verify_metrics = [0.0, 0.0, 0.0]

    # Run a for loop 1000 times to calculate averages
    for i in range(20):
        script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scripts', f'measure_{prefix}.sh')
        os.system(f'bash "{script_path}"')

        # Get metrics
        # Each returned list is [cpu_cycles, real_time, user_time, system_time]
        cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics = get_all_metrics(prefix)

        # Accumulate keypair metrics (private + public)
        # CPU cycles
        priv_cpu = int(private_metrics[0])
        pub_cpu = int(public_metrics[0])
        total_cpu = priv_cpu + pub_cpu
        avg_keypair_metrics[0] += (total_cpu - avg_keypair_metrics[0]) / (i+1)
        # Real time
        priv_real = float(private_metrics[1])
        pub_real = float(public_metrics[1])
        total_real = priv_real + pub_real
        avg_keypair_metrics[1] += (total_real - avg_keypair_metrics[1]) / (i+1)
        # User + System time = CPU time
        priv_usys = float(private_metrics[2]) + float(private_metrics[3])
        pub_usys = float(public_metrics[2]) + float(public_metrics[3])
        total_usys = priv_usys + pub_usys
        avg_keypair_metrics[2] += (total_usys - avg_keypair_metrics[2]) / (i+1)

        # Accumulate CSR metrics
        csr_cpu = int(csr_metrics[0])
        avg_csr_metrics[0] += (csr_cpu - avg_csr_metrics[0]) / (i+1)
        csr_real = float(csr_metrics[1])
        avg_csr_metrics[1] += (csr_real - avg_csr_metrics[1]) / (i+1)
        csr_usys = float(csr_metrics[2]) + float(csr_metrics[3])
        avg_csr_metrics[2] += (csr_usys - avg_csr_metrics[2]) / (i+1)

        # Accumulate CERT metrics
        cert_cpu = int(cert_metrics[0])
        avg_cert_metrics[0] += (cert_cpu - avg_cert_metrics[0]) / (i+1)
        cert_real = float(cert_metrics[1])
        avg_cert_metrics[1] += (cert_real - avg_cert_metrics[1]) / (i+1)
        cert_usys = float(cert_metrics[2]) + float(cert_metrics[3])
        avg_cert_metrics[2] += (cert_usys - avg_cert_metrics[2]) / (i+1)

        # Accumulate VERIFY metrics
        ver_cpu = int(verify_metrics[0])
        avg_verify_metrics[0] += (ver_cpu - avg_verify_metrics[0]) / (i+1)
        ver_real = float(verify_metrics[1])
        avg_verify_metrics[1] += (ver_real - avg_verify_metrics[1]) / (i+1)
        ver_usys = float(verify_metrics[2]) + float(verify_metrics[3])
        avg_verify_metrics[2] += (ver_usys - avg_verify_metrics[2]) / (i+1)


    return avg_keypair_metrics, avg_csr_metrics, avg_cert_metrics, avg_verify_metrics
