#!/usr/bin/env python3
import os
import re

def truncate_metric_records(content):
    """
    Truncate to the last 20 non-empty lines and remove leading spaces
    """
    if content is None:
        return None
    # Split and filter out empty/whitespace-only lines
    lines = [line for line in content.splitlines() if line.strip()]
    # Take the last 20 non-empty lines
    cleaned = lines[-20:]
    # Remove all leading spaces from each line
    cleaned = [line.lstrip() for line in cleaned]
    return "\n".join(cleaned)


def extract_timing_metrics(content):
    """
    Extract metrics: cpu_cycles, real_time, user_time, system_time
    """
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
        first = line.split(" ")[0]
        first = first.replace(",", "")
        return first

    idxs = [8, 17, 18, 19]
    cpu_cycles = extract_first_number(lines[idxs[0]])
    real_time = extract_first_number(lines[idxs[1]])
    user_time = extract_first_number(lines[idxs[2]])
    system_time = extract_first_number(lines[idxs[3]])
    result = [cpu_cycles, real_time, user_time, system_time]
    return result


def extract_memory_metrics(content):
    if content is None:
        return None
    # Remove all spaces from each line
    lines = [line.replace(' ', '') for line in content.splitlines()]
    # Remove empty lines
    lines = [line for line in lines if line]
    if not lines:
        return None
    # Return the last line as a string
    return str(lines[-1])


def get_all_metrics(prefix):
    """
    Given a prefix, returns a tuple of lists: (cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics)
    Each list contains [cpu_cycles, real_time, user_time, system_time] for the respective timing file.
    Returns None for any file that could not be processed.
    """
    timing_dir = os.path.join("results", f"{prefix}_times")
    memory_dir = os.path.join("results", f"{prefix}_memory")
    if not os.path.isdir(timing_dir):
        raise FileNotFoundError(f"Timing directory '{timing_dir}' does not exist.")
    if not os.path.isdir(memory_dir):
        raise FileNotFoundError(f"Memory directory '{memory_dir}' does not exist.")

    # Function to read a file and return its content
    def read_file(filename, parent_folder):
        path = os.path.join(parent_folder, filename)
        try:
            with open(path, "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            return None

    # Read and save contents of each timing file
    time_cert = read_file("time_cert.txt", timing_dir)
    time_csr = read_file("time_csr.txt", timing_dir)
    time_private = read_file("time_private.txt", timing_dir)
    time_public = read_file("time_public.txt", timing_dir)
    time_verify = read_file("time_verify.txt", timing_dir)

    mem_cert = read_file("mem_cert.txt", memory_dir)
    mem_csr = read_file("mem_csr.txt", memory_dir)
    mem_private = read_file("mem_private.txt", memory_dir)
    mem_public = read_file("mem_public.txt", memory_dir)
    mem_verify = read_file("mem_verify.txt", memory_dir)

    # Truncate and clean each file's content
    cleaned_cert = truncate_metric_records(time_cert)
    cleaned_csr = truncate_metric_records(time_csr)
    cleaned_private = truncate_metric_records(time_private)
    cleaned_public = truncate_metric_records(time_public)
    cleaned_verify = truncate_metric_records(time_verify)

    # Extract timing metrics from each cleaned content
    cert_metrics = extract_timing_metrics(cleaned_cert)
    csr_metrics = extract_timing_metrics(cleaned_csr)
    private_metrics = extract_timing_metrics(cleaned_private)
    public_metrics = extract_timing_metrics(cleaned_public)
    verify_metrics = extract_timing_metrics(cleaned_verify)

    # Extract memory metrics from each cleaned content and append to final metrics
    cert_memory = extract_memory_metrics(mem_cert)
    csr_memory = extract_memory_metrics(mem_csr)
    private_memory = extract_memory_metrics(mem_private)
    public_memory = extract_memory_metrics(mem_public)
    verify_memory = extract_memory_metrics(mem_verify)
    cert_metrics.append(cert_memory)
    csr_metrics.append(csr_memory)
    private_metrics.append(private_memory)
    public_metrics.append(public_memory)
    verify_metrics.append(verify_memory)

    # Return all metrics as a tuple
    return cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics

if __name__ == "__main__":
    """
    Main entry point when run as a script.
    """

    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "Extract timing metrics for a given prefix.\n"
            "It is assumed that the directory is named <prefix>_times and is located in the results directory.\n"
            " => Example: for prefix 'rsa', the directory would be 'results/rsa_times'."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--prefix", required=True, help="Prefix for the results directory (e.g., 'rsa')"
    )
    args = parser.parse_args()
    prefix = args.prefix
    cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics = (
        get_all_metrics(prefix)
    )
    print("\nLooks like i've been called from main... Extracted metrics:\n")
    print("\tcert:", cert_metrics)
    print("\tcsr:", csr_metrics)
    print("\tprivate:", private_metrics)
    print("\tpublic:", public_metrics)
    print("\tverify:", verify_metrics, "\n")
