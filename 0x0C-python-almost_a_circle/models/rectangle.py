#!/usr/bin/python3

""" This module is retangle class """

from models.base import Base


class Rectangle(Base):
    """ The is the class for the Rectangle object"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Intialization the Rectangle object with its Arguements """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @staticmethod
    def value_validator(key, value):
        """This function validate the type and value of the attribute"""
        if not isinstance(value, int):
            raise TypeError(f"{key} must be an integer")
        if key == 'width' or key == 'height':
            if value <= 0:
                raise ValueError(f"{key} must be > 0")
        if key == 'x' or key == 'y':
            if value < 0:
                raise ValueError(f"{key} must be >= 0")

    @property
    def width(self):
        """ get width attributes """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width attribute"""
        Rectangle.value_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """ get height attributes """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height attributes """
        Rectangle.value_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """ get x attributes"""
        return self.__x

    @x.setter
    def x(self, value):
        """ set x attribute """
        Rectangle.value_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """ get y property """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y attributes """
        Rectangle.value_validator('y', value)
        self.__y = value

    """ This is a area public instance """
    def area(self):
        """ This define the araa public instance """
        width = self.width
        height = self.height
        area = width * height
        return area

    """ This s a Display Public Object """
    def display(self):
        """ This function display the '#' stdout of the rectangle class"""
        width = self.__width
        height = self.__height
        for i in range(self.__y):
            print()
        for i in range(height):
            print(' ' * self.__x + '#' * width)

    """ Overriding str method"""
    def __str__(self):
        """ Return the string of the rectangle representation """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    """ This is the public  method to update """
    def update(self, *args, **kwargs):
        """ This function updates the class attributes with its arguements"""
        attribute_names = ('id', 'width', 'height', 'x', 'y')

        if args:
            for i, arg in enumerate(args):
                if i < len(attribute_names):
                    setattr(self, attribute_names[i], arg)

        for key, value in kwargs.items():
            if key in attribute_names:
                setattr(self, key, value)
