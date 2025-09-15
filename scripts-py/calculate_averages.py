#!/usr/bin/env python3

import sys
import os
import statistics

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "scripts-py"))
from extract_metrics import get_all_metrics  # type: ignore


# Function to calculate average metrics over a number of runs (default 1)
def calculate_averages(prefix, runs=1):
    """
    Runs the specified measurement script multiple times and calculates the running average for each metric.

    Args:
        prefix (str): The prefix used to select which measurement script to run (e.g., 'rsa', 'dilithium2').
        runs (int, optional): Number of times to run the measurement. Default is 1.

    Returns:
        tuple: Four lists, each containing three values (cpu_cycles, real_time, cpu_time) for:
            - keypair (combined private and public)
            - csr
            - cert
            - verify
        Each value is the average of the corresponding metric over all runs.
    """
    # Initialize metrics
    # Note: order is [cpu_cycles, real_time, cpu_time]
    avg_keypair = [0.0, 0.0, 0.0]
    avg_csr = [0.0, 0.0, 0.0]
    avg_cert = [0.0, 0.0, 0.0]
    avg_verify = [0.0, 0.0, 0.0]

    # Run for loop how many times specified by runs
    for i in range(runs):
        script_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "scripts",
            f"measure_{prefix}.sh",
        )
        os.system(f'bash "{script_path}"')

        # Get metrics
        # Each returned list is [cpu_cycles, real_time, user_time, system_time]
        cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics = (
            get_all_metrics(prefix)
        )

        # Accumulate keypair metrics (private + public)
        # CPU cycles
        priv_cpu = int(private_metrics[0])
        pub_cpu = int(public_metrics[0])
        total_cpu = priv_cpu + pub_cpu
        avg_keypair[0] += (total_cpu - avg_keypair[0]) / (i + 1)
        # Real time
        priv_real = float(private_metrics[1])
        pub_real = float(public_metrics[1])
        total_real = priv_real + pub_real
        avg_keypair[1] += (total_real - avg_keypair[1]) / (i + 1)
        # User + System time = CPU time
        priv_usys = float(private_metrics[2]) + float(private_metrics[3])
        pub_usys = float(public_metrics[2]) + float(public_metrics[3])
        total_usys = priv_usys + pub_usys
        avg_keypair[2] += (total_usys - avg_keypair[2]) / (i + 1)

        # Accumulate CSR metrics
        csr_cpu = int(csr_metrics[0])
        avg_csr[0] += (csr_cpu - avg_csr[0]) / (i + 1)
        csr_real = float(csr_metrics[1])
        avg_csr[1] += (csr_real - avg_csr[1]) / (i + 1)
        csr_usys = float(csr_metrics[2]) + float(csr_metrics[3])
        avg_csr[2] += (csr_usys - avg_csr[2]) / (i + 1)

        # Accumulate CERT metrics
        cert_cpu = int(cert_metrics[0])
        avg_cert[0] += (cert_cpu - avg_cert[0]) / (i + 1)
        cert_real = float(cert_metrics[1])
        avg_cert[1] += (cert_real - avg_cert[1]) / (i + 1)
        cert_usys = float(cert_metrics[2]) + float(cert_metrics[3])
        avg_cert[2] += (cert_usys - avg_cert[2]) / (i + 1)

        # Accumulate VERIFY metrics
        ver_cpu = int(verify_metrics[0])
        avg_verify[0] += (ver_cpu - avg_verify[0]) / (i + 1)
        ver_real = float(verify_metrics[1])
        avg_verify[1] += (ver_real - avg_verify[1]) / (i + 1)
        ver_usys = float(verify_metrics[2]) + float(verify_metrics[3])
        avg_verify[2] += (ver_usys - avg_verify[2]) / (i + 1)

    return avg_keypair, avg_csr, avg_cert, avg_verify


# Function to calculate median metrics over a number of runs (default 1)
def calculate_medians(prefix, runs=1):
    """
    Runs the specified measurement script multiple times and calculates the median for each metric.

    Args:
        prefix (str): The prefix used to select which measurement script to run (e.g., 'rsa', 'dilithium2').
        runs (int, optional): Number of times to run the measurement. Default is 1.

    Returns:
        tuple: Four lists, each containing three values (cpu_cycles, real_time, cpu_time) for:
            - keypair (combined private and public)
            - csr
            - cert
            - verify
        Each value is the median of the corresponding metric over all runs.
    """

    # Prepare lists to collect each metric over runs
    keypair_cpu = []
    keypair_real = []
    keypair_usys = []
    csr_cpu = []
    csr_real = []
    csr_usys = []
    cert_cpu = []
    cert_real = []
    cert_usys = []
    verify_cpu = []
    verify_real = []
    verify_usys = []

    # Run for loop how many times specified by runs
    for i in range(runs):
        script_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "scripts",
            f"measure_{prefix}.sh",
        )
        os.system(f'bash "{script_path}"')
        cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics = (
            get_all_metrics(prefix)
        )

        # Keypair: combine private + public
        priv_cpu = int(private_metrics[0])
        pub_cpu = int(public_metrics[0])
        keypair_cpu.append(priv_cpu + pub_cpu)
        priv_real = float(private_metrics[1])
        pub_real = float(public_metrics[1])
        keypair_real.append(priv_real + pub_real)
        priv_usys = float(private_metrics[2]) + float(private_metrics[3])
        pub_usys = float(public_metrics[2]) + float(public_metrics[3])
        keypair_usys.append(priv_usys + pub_usys)

        # CSR metrics
        csr_cpu.append(int(csr_metrics[0]))
        csr_real.append(float(csr_metrics[1]))
        csr_usys.append(float(csr_metrics[2]) + float(csr_metrics[3]))

        # CERT metrics
        cert_cpu.append(int(cert_metrics[0]))
        cert_real.append(float(cert_metrics[1]))
        cert_usys.append(float(cert_metrics[2]) + float(cert_metrics[3]))

        # VERIFY metrics
        verify_cpu.append(int(verify_metrics[0]))
        verify_real.append(float(verify_metrics[1]))
        verify_usys.append(float(verify_metrics[2]) + float(verify_metrics[3]))

    # Compute medians
    med_keypair = [
        statistics.median(keypair_cpu),
        statistics.median(keypair_real),
        statistics.median(keypair_usys),
    ]
    med_csr = [
        statistics.median(csr_cpu),
        statistics.median(csr_real),
        statistics.median(csr_usys),
    ]
    med_cert = [
        statistics.median(cert_cpu),
        statistics.median(cert_real),
        statistics.median(cert_usys),
    ]
    med_verify = [
        statistics.median(verify_cpu),
        statistics.median(verify_real),
        statistics.median(verify_usys),
    ]

    return med_keypair, med_csr, med_cert, med_verify
