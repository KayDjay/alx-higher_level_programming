#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_set = []
    for a in set_1:
        if a in set_2:
            new_set.append(a)
    return new_set
