# For Ubuntu/Debian based systems using the apt package manager
# Installs packages required for building liboqs, OpenSSL, and the provider

echo -e "\033[1;31mIMPORTANT:\033[0m sudo access is required to install dependencies."
echo "You may be prompted for your password."
sudo apt update
sudo apt install -y build-essential cmake git
