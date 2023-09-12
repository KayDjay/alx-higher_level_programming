#!/usr/bin/python3

"""Module to checks if an object is an instance of a
class or of an inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Check for objects is an instance or a class that inherited from,
    the specified clasis
    Args:
        obj (obj): the object to check
        a_class (obj): The class to check against
    Returns:
        boolean: True or False
    """

    return True if isinstance(obj, a_class) else False
