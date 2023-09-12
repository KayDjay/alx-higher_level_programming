#!/usr/bin/python3

"""
This is the module for the child class MyList
"""


class MyList(list):
    """
    This is the child class MyList

    Inherits from list module
    """
    def print_sorted(self):
        """ Print_sorted function """
        print(sorted(self))
