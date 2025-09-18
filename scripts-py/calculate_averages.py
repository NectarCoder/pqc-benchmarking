#!/usr/bin/env python3

import subprocess
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
        tuple: Four lists, each containing four values [cpu_cycles, real_time, cpu_time, memrss] for:
            - keypair (combined private and public)
            - csr
            - cert
            - verify
        Each value is the running average of the corresponding metric over all runs.
    """
    # Initialize metrics
    # Note: order is [cpu_cycles, real_time, cpu_time, memrss]
    avg_keypair = [0.0, 0.0, 0.0, 0.0]
    avg_csr     = [0.0, 0.0, 0.0, 0.0]
    avg_cert    = [0.0, 0.0, 0.0, 0.0]
    avg_verify  = [0.0, 0.0, 0.0, 0.0]

    # Run for loop how many times specified by runs
    for i in range(runs):
        script_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "scripts",
            f"measure_{prefix}.sh",
        )
        # os.system(f'bash "{script_path}"')
        subprocess.run(["bash", script_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        # Get metrics
        # Each returned list is [cpu_cycles, real_time, user_time, system_time, memrss]
        cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics = (
            get_all_metrics(prefix)
        )        

        # Accumulate keypair metrics (private + public)
        # CPU cycles
        priv_cpu_cycles = int(private_metrics[0])
        pub_cpu_cycles = int(public_metrics[0])
        total_cpu_cycles = priv_cpu_cycles + pub_cpu_cycles
        avg_keypair[0] += (total_cpu_cycles - avg_keypair[0]) / (i + 1)
        # Real time
        priv_real = float(private_metrics[1])
        pub_real = float(public_metrics[1])
        total_real = priv_real + pub_real
        avg_keypair[1] += (total_real - avg_keypair[1]) / (i + 1)
        # User time + Sys time = CPU time
        priv_cpu_time = float(private_metrics[2]) + float(private_metrics[3])
        pub_cpu_time  = float(public_metrics[2]) + float(public_metrics[3])
        total_time = priv_cpu_time + pub_cpu_time
        avg_keypair[2] += (total_time - avg_keypair[2]) / (i + 1)
        # Memory RSS
        priv_mem  = int(private_metrics[4])
        pub_mem   = int(public_metrics[4])
        total_mem = priv_mem + pub_mem
        avg_keypair[3] += (total_mem - avg_keypair[3]) / (i + 1)

        # Accumulate CSR metrics
        # CPU cycles
        csr_cpu_cycles = int(csr_metrics[0])
        avg_csr[0] += (csr_cpu_cycles - avg_csr[0]) / (i + 1)
        # Real time
        csr_real = float(csr_metrics[1])
        avg_csr[1] += (csr_real - avg_csr[1]) / (i + 1)
        # User time + Sys time = CPU time
        csr_cpu_time = float(csr_metrics[2]) + float(csr_metrics[3])
        avg_csr[2] += (csr_cpu_time - avg_csr[2]) / (i + 1)
        # Memory RSS
        csr_mem = int(csr_metrics[4])
        avg_csr[3] += (csr_mem - avg_csr[3]) / (i + 1)

        # Accumulate CERT metrics
        # CPU cycles
        cert_cpu_cycles = int(cert_metrics[0])
        avg_cert[0] += (cert_cpu_cycles - avg_cert[0]) / (i + 1)
        # Real time
        cert_real = float(cert_metrics[1])
        avg_cert[1] += (cert_real - avg_cert[1]) / (i + 1)
        # User time + Sys time = CPU time
        cert_cpu_time = float(cert_metrics[2]) + float(cert_metrics[3])
        avg_cert[2] += (cert_cpu_time - avg_cert[2]) / (i + 1)
        # Memory RSS
        cert_mem = int(cert_metrics[4])
        avg_cert[3] += (cert_mem - avg_cert[3]) / (i + 1)

        # Accumulate VERIFY metrics
        # CPU cycles
        ver_cpu_cycles = int(verify_metrics[0])
        avg_verify[0] += (ver_cpu_cycles - avg_verify[0]) / (i + 1)
        # Real time
        ver_real = float(verify_metrics[1])
        avg_verify[1] += (ver_real - avg_verify[1]) / (i + 1)
        # User time + Sys time = CPU time
        ver_cpu_time = float(verify_metrics[2]) + float(verify_metrics[3])
        avg_verify[2] += (ver_cpu_time - avg_verify[2]) / (i + 1)
        # Memory RSS
        ver_mem = int(verify_metrics[4])
        avg_verify[3] += (ver_mem - avg_verify[3]) / (i + 1)

    # For CPU cycles and memrss, convert to int for final output
    avg_keypair[0] = int(avg_keypair[0])
    avg_keypair[3] = int(avg_keypair[3])
    avg_csr[0]     = int(avg_csr[0])
    avg_csr[3]     = int(avg_csr[3])
    avg_cert[0]    = int(avg_cert[0])
    avg_cert[3]    = int(avg_cert[3])
    avg_verify[0]  = int(avg_verify[0])
    avg_verify[3]  = int(avg_verify[3])

    # Convert real_time and cpu_time to milliseconds (from seconds)
    avg_keypair[1] *= 1000.0
    avg_keypair[2] *= 1000.0
    avg_csr[1]     *= 1000.0
    avg_csr[2]     *= 1000.0
    avg_cert[1]    *= 1000.0
    avg_cert[2]    *= 1000.0
    avg_verify[1]  *= 1000.0
    avg_verify[2]  *= 1000.0

    # Return the averages
    return avg_keypair, avg_csr, avg_cert, avg_verify


# Function to calculate median metrics over a number of runs (default 1)
def calculate_medians(prefix, runs=1):
    """
    Runs the specified measurement script multiple times and calculates the median for each metric.

    Args:
        prefix (str): The prefix used to select which measurement script to run (e.g., 'rsa', 'dilithium2').
        runs (int, optional): Number of times to run the measurement. Default is 1.

    Returns:
        tuple: Four lists, each containing four values [cpu_cycles, real_time, cpu_time, memrss] for:
            - keypair (combined private and public)
            - csr
            - cert
            - verify
        Each value is the median of the corresponding metric over all runs.
    """

    # Prepare lists to collect each metric over runs
    # Note: order in results is [cpu_cycles, real_time, cpu_time, memrss]
    keypair_cpu_cycles = []
    keypair_real = []
    keypair_cpu_time = []
    keypair_mem = []
    csr_cpu = []
    csr_real = []
    csr_time = []
    csr_mem = []
    cert_cpu = []
    cert_real = []
    cert_time = []
    cert_mem = []
    verify_cpu = []
    verify_real = []
    verify_time = []
    verify_mem = []

    # Run for loop how many times specified by runs
    for i in range(runs):
        script_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "scripts",
            f"measure_{prefix}.sh",
        )
        # os.system(f'bash "{script_path}"')
        subprocess.run(["bash", script_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics = (
            get_all_metrics(prefix)
        )

        # Keypair: combine private + public
        # CPU cycles
        priv_cpu_cycles = int(private_metrics[0])
        pub_cpu_cycles = int(public_metrics[0])
        keypair_cpu_cycles.append(priv_cpu_cycles + pub_cpu_cycles)
        # Real time
        priv_real = float(private_metrics[1])
        pub_real = float(public_metrics[1])
        keypair_real.append(priv_real + pub_real)
        # User time + Sys time = CPU time
        priv_time = float(private_metrics[2]) + float(private_metrics[3])
        pub_time = float(public_metrics[2]) + float(public_metrics[3])
        keypair_cpu_time.append(priv_time + pub_time)
        # Memory RSS
        priv_mem = int(private_metrics[4])
        pub_mem = int(public_metrics[4])
        keypair_mem.append(priv_mem + pub_mem)

        # CSR metrics
        csr_cpu.append(int(csr_metrics[0]))
        csr_real.append(float(csr_metrics[1]))
        csr_time.append(float(csr_metrics[2]) + float(csr_metrics[3]))
        csr_mem.append(int(csr_metrics[4]))

        # CERT metrics
        cert_cpu.append(int(cert_metrics[0]))
        cert_real.append(float(cert_metrics[1]))
        cert_time.append(float(cert_metrics[2]) + float(cert_metrics[3]))
        cert_mem.append(int(cert_metrics[4]))

        # VERIFY metrics
        verify_cpu.append(int(verify_metrics[0]))
        verify_real.append(float(verify_metrics[1]))
        verify_time.append(float(verify_metrics[2]) + float(verify_metrics[3]))
        verify_mem.append(int(verify_metrics[4]))

    # Compute medians
    med_keypair = [
        statistics.median(keypair_cpu_cycles),
        statistics.median(keypair_real),
        statistics.median(keypair_cpu_time),
        statistics.median(keypair_mem),
    ]
    med_csr = [
        statistics.median(csr_cpu),
        statistics.median(csr_real),
        statistics.median(csr_time),
        statistics.median(csr_mem),
    ]
    med_cert = [
        statistics.median(cert_cpu),
        statistics.median(cert_real),
        statistics.median(cert_time),
        statistics.median(cert_mem),
    ]
    med_verify = [
        statistics.median(verify_cpu),
        statistics.median(verify_real),
        statistics.median(verify_time),
        statistics.median(verify_mem),
    ]

    # For CPU cycles and memrss, convert to int for final output
    med_keypair[0] = int(med_keypair[0])
    med_keypair[3] = int(med_keypair[3])
    med_csr[0]     = int(med_csr[0])
    med_csr[3]     = int(med_csr[3])
    med_cert[0]    = int(med_cert[0])
    med_cert[3]    = int(med_cert[3])
    med_verify[0]  = int(med_verify[0])
    med_verify[3]  = int(med_verify[3])

    # Convert real_time and cpu_time to milliseconds (from seconds)
    med_keypair[1] *= 1000.0
    med_keypair[2] *= 1000.0
    med_csr[1]     *= 1000.0
    med_csr[2]     *= 1000.0
    med_cert[1]    *= 1000.0
    med_cert[2]    *= 1000.0
    med_verify[1]  *= 1000.0
    med_verify[2]  *= 1000.0

    # Return the medians
    return med_keypair, med_csr, med_cert, med_verify
