#!/bin/bash
# Bash script takes in a URL and display the HTTP methods
curl -s -I "$1" | awk -F ': ' '/^Allow:/ {print $2}'
