#!/usr/bin/python3

""" Define a class square """


class Square:
    """ Initializes the class object with a size attribute """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):

        """ Gets the size of the instance """
        return self.__size

    @size.setter
    def size(self, size):
        """ Set the size of the square """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

            """ Public area attribute """
    def area(self):
        return self.__size ** 2

        """ Public instance print """

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self. __size):
                for j in range(self.__size):
                    print("#", end="")
                print()
