#!/usr/bin/env python3
import os
import sys

# Add the scripts-py directory to sys.path and import get_all_metrics
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts-py'))
from extract_timing_metrics import get_all_metrics  # type: ignore

if __name__ == "__main__":
    prefix = 'rsa'
    cert_metrics, csr_metrics, private_metrics, public_metrics, verify_metrics = get_all_metrics(prefix)
    print("cert:", cert_metrics)
    print("csr:", csr_metrics)
    print("private:", private_metrics)
    print("public:", public_metrics)
    print("verify:", verify_metrics)
