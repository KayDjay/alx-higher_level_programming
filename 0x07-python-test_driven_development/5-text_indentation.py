#!/usr/bin/python3

""" Define a function that prints text indentation """


def text_indentation(text):
    """
    Params:
        text: the string of text to be properly indented

    Raise:
        TypeError: text must be a string

    Return:
        A text of formated string
    """
    mark = ['.', '?', ':']
    new_text = str()

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        if i in mark:
            new_text += i + '\n\n'
        else:
            new_text += i

    print(new_text.strip(), end='')
