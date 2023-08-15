#!/usr/bin/env python3
def no_c(my_string):
    rm_str = 'cC'
    new_str = ''
    for a in my_string:
        if a not in rm_str:
            new_str += a
    return new_str
