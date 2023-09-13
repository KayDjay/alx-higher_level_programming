#!/usr/bin/python3

"""
This is the module for Rectangle class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ This is a child class inherited from BaseGeometry """
    def __init__(self, width, height):
        """
        Initialize the instance

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        """Area public instance"""
    def area(self):
        return self.__height * self.__width

        """ string public instance"""
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
