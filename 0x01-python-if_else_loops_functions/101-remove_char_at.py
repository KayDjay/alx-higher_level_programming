#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    for s in range(len(str)):
        if s != n:
            copy += str[s]
    return copy
