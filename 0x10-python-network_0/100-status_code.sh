#!/bin/bash
# Bash script to display http status code response
curl -s -w "%{http_code}" -o /dev/null "$1"
