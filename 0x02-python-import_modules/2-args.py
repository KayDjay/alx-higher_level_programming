#!/usr/bin/python3
from sys import argv

num = len( argv) - 1

__name__ = "__main__"

if num == 0:
    print(f"{num} arguments.")
elif num == 1:
    print(f"{num} argument:")
else:
    print(f"{num} arguments:")

for a in range(1, num + 1):
    print(f"{a}: {argv[a]}")
