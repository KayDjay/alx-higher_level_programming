#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if chr(a) not in ['q', 'e']:
        print("{:s}".format(chr(a)), end='')
