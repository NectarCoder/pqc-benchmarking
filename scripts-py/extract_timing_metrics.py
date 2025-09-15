#!/usr/bin/env python3
import os
import re

"""
Truncate to the last 20 non-empty lines and remove leading spaces
"""
def truncate_metric_records(content, file_type):
    if content is None:
        return None
    # Split and filter out empty/whitespace-only lines
    lines = [line for line in content.splitlines() if line.strip()]
    # Take the last 20 non-empty lines
    cleaned = lines[-20:]
    # Remove all leading spaces from each line
    cleaned = [line.lstrip() for line in cleaned]
    return '\n'.join(cleaned)

"""
Extract metrics: cpu_cycles, real_time, user_time, system_time
"""
def extract_metrics(content, label=None):
    # Defensive: ensure content is not None
    if content is None:
        return None
    lines = content.splitlines()

    # Defensive: ensure at least 20 lines
    if len(lines) < 20:
        return None

    # Extract the first number from a line, removing any commas
    def extract_first_number(line):
        line = re.sub(r"\s+", " ", line.strip())
        first = line.split(' ')[0]
        first = first.replace(",", "")
        return first

    idxs = [8, 17, 18, 19]
    cpu_cycles = extract_first_number(lines[idxs[0]])
    real_time = extract_first_number(lines[idxs[1]])
    user_time = extract_first_number(lines[idxs[2]])
    system_time = extract_first_number(lines[idxs[3]])
    result = [cpu_cycles, real_time, user_time, system_time]
    return result

"""
Given a prefix, returns a tuple of lists: (cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics)
Each list contains [cpu_cycles, real_time, user_time, system_time] for the respective timing file.
Returns None for any file that could not be processed.
"""
def get_all_metrics(prefix):
    timing_dir = os.path.join("results", f"{prefix}_times")
    if not os.path.isdir(timing_dir):
        raise FileNotFoundError(f"Timing directory '{timing_dir}' does not exist.")

    # Function to read a file and return its content
    def read_file(filename):
        path = os.path.join(timing_dir, filename)
        try:
            with open(path, "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            return None

    # Read and save contents of each timing file
    time_cert = read_file("time_cert.txt")
    time_csr = read_file("time_csr.txt")
    time_private = read_file("time_private.txt")
    time_public = read_file("time_public.txt")
    time_verify = read_file("time_verify.txt")

    # Truncate and clean each file's content
    cleaned_cert = truncate_metric_records(time_cert, 'cert')
    cleaned_csr = truncate_metric_records(time_csr, 'csr')
    cleaned_private = truncate_metric_records(time_private, 'private')
    cleaned_public = truncate_metric_records(time_public, 'public')
    cleaned_verify = truncate_metric_records(time_verify, 'verify')

    # Extract metrics from each cleaned content
    cert_metrics = extract_metrics(cleaned_cert, label="time_cert")
    csr_metrics = extract_metrics(cleaned_csr, label="time_csr")
    private_metrics = extract_metrics(cleaned_private, label="time_private")
    public_metrics = extract_metrics(cleaned_public, label="time_public")
    verify_metrics = extract_metrics(cleaned_verify, label="time_verify")

    # Return all metrics as a tuple
    return cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics

"""
Main entry point when run as a script.
"""
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description=(
            "Extract timing metrics for a given prefix.\n"
            "It is assumed that the directory is named <prefix>_times and is located in the results directory.\n"
            " => Example: for prefix 'rsa', the directory would be 'results/rsa_times'."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--prefix", required=True, help="Prefix for the results directory (e.g., 'rsa')")
    args = parser.parse_args()
    prefix = args.prefix
    cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics = get_all_metrics(prefix)
    print("\nLooks like i've been called from main... Extracted metrics:\n")
    print("\tcert:", cert_metrics)
    print("\tcsr:", csr_metrics)
    print("\tprivate:", private_metrics)
    print("\tpublic:", public_metrics)
    print("\tverify:", verify_metrics, "\n")
