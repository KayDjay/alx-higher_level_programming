#!/usr/bin/python3

""" This module add new attribute to object instance """


def add_attribute(obj, name, value):
    """
    Define add_attribute function

    Args:
        name: attribute to be added
        value: value of new attibutes to be added
        """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
