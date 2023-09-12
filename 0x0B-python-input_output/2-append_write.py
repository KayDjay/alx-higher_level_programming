#!/usr/bin/python3

"""
This module is to append a string at the end of text file """


def append_write(filename="", text=""):
    """
    This function append text to a file

    Params:
        filename: file to create or append text to
        text: text to append to filename

    Return: content of the file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        content = f.write(text)
        return content
