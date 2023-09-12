#!/usr/bin/python3
"""Module that has an empty class BaseGeometry
"""


class BaseGeometry:
    """ BaseGeometry Class """

    def area(self):
        """ Raise and exception that area is not implemented """
        raise Exception("area() is not implemented")
