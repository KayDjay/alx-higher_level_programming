#!/usr/bin/python3
"""Module that has an empty class BaseGeometry
"""


class BaseGeometry:
    """ BaseGeometry Class """

    def area(self):
        """ Raise and exception that area is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This is  define integer validator and raises exceptions """
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
