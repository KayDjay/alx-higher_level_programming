#!/usr/bin/python3
""" This module is about Base class and its attributes """


class Base:
    """ This is the Base Object """

    # private class attribute
    __nb_objects = 0

    # Constructor
    def __init__(self, id=None):

        """ Initialization of the objects of id """
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = self.__nb_objects

    @property
    def id(self):
        """ get the ID """
        return self.__id

    @id.setter
    def id(self, value):
        """ setter id """
        self.__id = value
