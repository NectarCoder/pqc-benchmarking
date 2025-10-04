#!/usr/bin/env bash
# Centralized color helpers for test scripts.
# Sets COLOR_* variables when stdout is a TTY and TERM is not 'dumb'.

_tests_colors_init() {
    # Default to no color
    COLOR_RESET=""
    COLOR_OK=""
    COLOR_ERR=""
    COLOR_INFO=""
    COLOR_HDR=""

    # Allow users to override disabling colors with NO_COLOR
    if [ -t 1 ] && [ "${TERM:-}" != "dumb" ] && [ -z "${NO_COLOR:-}" ]; then
        COLOR_RESET="\x1b[0m"
        COLOR_OK="\x1b[32m"    # green
        COLOR_ERR="\x1b[31m"   # red
        COLOR_INFO="\x1b[33m"  # yellow
        COLOR_HDR="\x1b[36;1m" # bright cyan / bold for headers
    fi
}

_tests_colors_init

export COLOR_RESET COLOR_OK COLOR_ERR COLOR_INFO COLOR_HDR
