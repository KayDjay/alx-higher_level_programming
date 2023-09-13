#!/usr/bin/python3
""" This module return the dictionary with simple data structure """

def class_to_json(obj):
    """ Describe  the instance of object and its attributes """
    return obj.__dict__
