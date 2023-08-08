#!/usr/bin/env python3
def uppercase(str):
    for a in range(len(str)):
        print("{}".format(chr(ord(str[a]) - 32)
              if ord(str[a]) >= 97
              and ord(str[a]) <= 122 else str[a]), end='')
    print()
