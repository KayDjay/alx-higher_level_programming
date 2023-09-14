#!/usr/bin/python3

"""
This module add all arguement to a list and save the list to a file.
"""

import sys
from os import path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filepath = 'add_item.json'
data = []

try:
    data = load_from_json_file(filepath)
except FileNotFoundError:
    with open(filepath, 'w') as f:
        data

data.extend(sys.argv[1:])

save_to_json_file(data, filepath)
