#!/usr/bin/python3

""" This is a  Square class module inherits from Rectangle class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This  is a square object that inherit from rectangle class """
    def __init__(self, size):
        """ Initialize with the size of square """
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)
