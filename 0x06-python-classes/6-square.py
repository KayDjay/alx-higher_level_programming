#!/usr/bin/python3

""" Define a class Square """


class Square:
    """
    Initializes the class object with a size and position attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):

        """ Gets the size of the instance """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif  value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ The position of square """
        return self.position

    @position.setter
    def position(self, value):
        """ Set the postion of the square """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

            """ Public area attribute """
    def area(self):
        return self.__size ** 2

        """ Public instance that print the square character  """

    def my_print(self):

        if self.__size == 0:
            print()
            return
        for a in range(self.__position[1]):
            print()
        for b in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
