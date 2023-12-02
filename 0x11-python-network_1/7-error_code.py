#!/usr/bin/python3
"""
python script that fetches URLs request and return error if any
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    request = requests.get(url)
    if requests.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
