#!/usr/bin/python3
""" Python script that fetches URLs request """

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as request:
        html = request.read()
        x_request_id = request.headers['X-Request-Id']
        print(f"{x_request_id}")
