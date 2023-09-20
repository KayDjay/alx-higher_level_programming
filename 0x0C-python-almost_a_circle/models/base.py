#!/usr/bin/python3
""" This module is about Base class and its attributes """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This function return the list dictionaries JSON string rep """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ This is to writes JSON string of lists_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                new_file = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(new_file))

    @staticmethod
    def from_json_string(json_string):
        """ This function returns the list of JSON string representation """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ This function return the set attributes to the instances"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ This function that returns a list of instances from csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename) as f:
                dict_reader = DictReader(f)
                list_dict = list(dict_reader)
            return list_dict

        except FileNotFoundError:
            return[]
