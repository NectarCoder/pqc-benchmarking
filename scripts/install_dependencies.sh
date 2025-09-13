#!/bin/bash

# For Ubuntu/Debian based systems using the apt package manager
# Installs dependencies required for building OpenSSL, liboqs, and oqs-provider

echo -e "IMPORTANT: sudo access is required to install dependencies.";
echo "You may be prompted for your password."
sudo apt update
sudo apt install -y build-essential cmake git ninja-build python3 python-is-python3 python3-pip curl wget

# List of dependencies
# - build-essential
# - cmake
# - git
# - ninja-build
# - python3
# - python-is-python3
# - python3-pip
# - curl
# - wget