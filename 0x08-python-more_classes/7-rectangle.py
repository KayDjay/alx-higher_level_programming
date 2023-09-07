#!/usr/bin/python3
"""
Defines Rectangle class
"""


class Rectangle:
    """ Initializing Rectangle with width and height """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Public area of a rectangle attribute """
        return self.__width * self.__height

    def perimeter(self):
        """ Public perimeter of a rectangle attribute """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ return string rectangle"""
        width = self.__width
        height = self.__height
        ret = ''
        if width == 0 or height == 0:
            ret
        else:
            a = self.print_symbol
            ret  = '{}{}'.format((str(a) * width + '\n') * (height - 1),
                                str(a) * width)
            return ret

    def __repr__(self):
        """ return string representation """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ deleting an instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
