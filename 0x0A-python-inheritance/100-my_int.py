#!/usr/bin/python3
""" This module is MyInt """


class MyInt(int):
    """ The MyInt object inherit from int method """

    def __eq__(self, other):
        """ define the equality private instance """
        return super().__ne__(other)

    def __ne__(self, other):
        """ define the not equal private instance """
        return super().__eq__(other)
