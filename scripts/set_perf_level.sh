#!/bin/bash

# Sets the perf_event_paranoid level to 1 to allow user-level access.

echo -e "IMPORTANT: sudo access is required to set the performance level."
echo "You may be prompted for your password."

# Define the configuration file path
CONF_FILE="/etc/sysctl.d/99-perf-paranoid.conf"

echo -n "Current level: "; cat /proc/sys/kernel/perf_event_paranoid

# Set paranoid level to 1 for the current session to allow user access
echo "Setting live paranoid level to 1..."
sudo sysctl -w kernel.perf_event_paranoid=1 >/dev/null

# Make the setting persistent across reboots by writing it to a conf file
echo "Creating/updating persistent configuration file ($CONF_FILE)..."
echo "kernel.perf_event_paranoid = 1" | sudo tee "$CONF_FILE" >/dev/null

echo -n "Updated level: "; cat /proc/sys/kernel/perf_event_paranoid