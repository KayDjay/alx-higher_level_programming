#!/usr/bin/python3

"""
This module is to writes a string to a text file """


def write_file(filename="", text=""):
    """
    This function write content to a file

    Params:
        filename: file to create or write to
        text: text to write to filename

    Return: content of the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        content = f.write(text)
        return content
