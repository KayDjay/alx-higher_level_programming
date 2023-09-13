#!/usr/bin/python3
""" This Module is a Square class inherits from Rectangle class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This is a square object that inherit from Rectangle """
    def __init__(self, size):
        """ Initialize the square class with a size """
        self.__size = size
        self.integer_validator('size', size)

    """ Area public instance """
    def area(self):
        return self.__size ** 2

    """String public  instance """
    def __str__(self):
        return f'[square] {self.__size}/{self.__size}'
