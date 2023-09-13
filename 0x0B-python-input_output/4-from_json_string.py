#!/usr/bin/python3
""" This module returns an object represented by JSON string """

import json

def from_json_string(my_str):
    """ This function get string from json """
    return json.loads(my_str)
