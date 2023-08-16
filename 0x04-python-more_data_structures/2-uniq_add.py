#!/usr/bin/python3

def uniq_add(my_list=[]):
    if not my_list:
        return 0

    new_list = set(my_list)
    result = 0
    for a in new_list:
        result += a
    return result
