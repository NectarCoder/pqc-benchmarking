#!/usr/bin/bash

# For Ubuntu/Debian based systems using the apt package manager
# Installs dependencies required for building OpenSSL, liboqs, and oqs-provider

echo -e "IMPORTANT: sudo access is required to install dependencies.";
echo "You may be prompted for your password."
sudo apt update
sudo apt install -y build-essential cmake git ninja-build curl wget astyle gcc libssl-dev libgmp3-dev unzip xsltproc doxygen graphviz valgrind
sudo apt install -y python3 python-is-python3 python3-pip python3-pytest python3-pytest-xdist python3-tabulate python3-yaml
sudo apt install -y linux-tools-common linux-tools-generic linux-tools-$(uname -r)

# List of dependencies (in the same order as the install commands)
# - build-essential
# - cmake
# - git
# - ninja-build
# - curl
# - wget
# - astyle
# - gcc
# - libssl-dev
# - libgmp3-dev
# - unzip
# - xsltproc
# - doxygen
# - graphviz
# - valgrind
# - python3
# - python-is-python3
# - python3-pip
# - python3-pytest
# - python3-pytest-xdist
# - python3-tabulate
# - python3-yaml
