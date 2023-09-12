#!/usr/bin/python3

"""
Module Inherited from
Checks if the object of a class
inherited directly or indirectly from specified class
"""


def inherits_from(obj, a_class):
    """ check if the object inherit from a class
    Args:
        obj: the object to check
        a-class: the class to check against
    Returns:
    boolean: True or false
    """

    return isinstance(obj, a_class) and not (type(obj) is a_class)
