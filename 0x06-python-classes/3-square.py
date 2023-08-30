#!/usr/bin/python3

""" Define a class Square """


class Square:

    """" initializing an object and arguements """
    def __init__(self, size=0):

        if type(size) != int:
            raise TypeError("size mut be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        """ Define public attribute area """
    def area(self):
        return self.__size ** 2
