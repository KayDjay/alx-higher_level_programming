#!/usr/bin/python3

""" This module creates an object from a json file """

import json


def load_from_json_file(filename):
    """
    This function load file from json

    Params:
        filename: the file to load

    Return:
        loaded JSOn file
    """
    with open(filename, encoding='utf-8') as f:
        content = f.read()
        load = json.loads(content)
        return load
