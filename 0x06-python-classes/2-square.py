#!/usr/bin/python3

''' Define a square class '''


class Square:

    """ Initialized an object with the size of square """

    def __init__(self, size=0):

        """ If statement and its arguement """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
