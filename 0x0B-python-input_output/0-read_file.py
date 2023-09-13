#!/usr/bin/python3

""" This module read encoding text and print """


def read_file(filename=""):
    """ This function read text file
    Args:
        Filename to be read
        Return: print the file content """

    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
        print(content, end='')
