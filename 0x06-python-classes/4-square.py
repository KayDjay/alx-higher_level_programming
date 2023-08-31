#!/usr/bin/python3

""" Define a class Square """


class Square:

    """ Initialising class object with size attibutes
            and its size arguements """

    def __init__(self, size=0):

        """ initializes size of self with self  """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        """ If statement and its arguement """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        """ Define public attribute area """

    def area(self):
        return self.__size ** 2
