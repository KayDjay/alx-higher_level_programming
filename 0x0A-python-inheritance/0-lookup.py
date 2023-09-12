#!/usr/bin/python3

"""
Lookup function Module
"""


def lookup(obj):
    """
    This is the lookup function

    Params:
        obj: object to lookup
    Return:
        list of all method of object
    """
    return dir(obj)
