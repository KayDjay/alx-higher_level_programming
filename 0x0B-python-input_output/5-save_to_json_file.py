#!/usr/bin/python3

""" This is the module writes an Object to text file """

import json


def save_to_json_file(my_obj, filename):
    """
    This function to save object in json to filename

    Params:
        my_obj: JSON object to write to file
        filename: file to write to

    Return:
        JSON OBJECT in filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        content = json.dumps(my_obj)
        save = f.write(content)
        return save  
