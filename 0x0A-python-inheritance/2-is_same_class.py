#!/usr/bin/python3
"""
Module to check if an object is an instance
of specified class
"""


def is_same_class(obj, a_class):
    """ Check the parameters of the class
    Args:
        obj (obj): the object to check
        a_class (obj): The class to check against
    Returns:
        bool: return True or false
            """

    return True if type(obj) is a_class else False
