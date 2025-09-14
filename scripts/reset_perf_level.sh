#!/bin/bash

# Reverts the perf_event_paranoid setting to the system default (Level 4 on Ubuntu 24+).

echo -e "IMPORTANT: sudo access is required to revert the performance level.";
echo "You may be prompted for your password.";

# Define the configuration file path
CONF_FILE="/etc/sysctl.d/99-perf-paranoid.conf"

echo -n "Current level: "; cat /proc/sys/kernel/perf_event_paranoid

# Set paranoid level back to 4 (common default, requires sudo for kernel profiling)
echo "Reverting live setting to default value of 4..."
sudo sysctl -w kernel.perf_event_paranoid=4 >/dev/null

# Remove the persistent configuration file if it exists
if [ -f "$CONF_FILE" ]; then
    echo "Removing persistent configuration file ($CONF_FILE)..."
    sudo rm "$CONF_FILE"
else
    echo "No persistent configuration file found to remove."
fi

echo -n "Updated level: "; cat /proc/sys/kernel/perf_event_paranoid