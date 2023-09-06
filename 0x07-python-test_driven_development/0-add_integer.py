#!/usr/bin/python3

""" Define add function """


def add_integer(a, b=98):
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
