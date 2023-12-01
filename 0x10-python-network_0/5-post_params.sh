#!/bin/bash
# Bash script that send a POST [an email and subject]
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
