#!/usr/bin/python3
""" This module returns JSON representation of an object """

import json


def to_json_string(my_obj):
    """ This function get string from json """
    return json.dumps(my_obj)
