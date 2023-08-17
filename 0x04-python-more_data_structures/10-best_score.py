#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_score = 0
    name = ''
    for a, b in a_dictionary.items():
        if b > best_score:
            best_score = b
            name = a
    return name
