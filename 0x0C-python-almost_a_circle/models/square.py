#!/usr/bin/python3

"""
This is the module for square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is the square object """
    # Constructor
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the sqaure objects with its arguements """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of square"""
        s = self.width
        x = self.x
        y = self.y
        d = self.id
        return f"[Square] ({d}) {x}/{y} - {s1}"

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """This set the value of size by using rectangle class attributes """
        self.width = value
        self.height = value

    """ Update Public method """
    def update(self, *args, **kwargs):
        """ This updates the square class attributes """
        attribute_names = ('id', 'size', 'x', 'y')

        if args:
            for i, arg in enumerate(args):
                if i < len(attribute_names):
                    setattr(self, attribute_names[i], arg)

        for key, value in kwargs.items():
            if key in attribute_names:
                setattr(self, key, value)

     """Dictionary Public Instance """
    def to_dictionary(self):
        """
        this method return a dictionary of the square
        """
    return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.width}
