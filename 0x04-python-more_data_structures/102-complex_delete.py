#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    if value not in a_dictionary.values():
        return a_dictionary

    key_del = []
    for keys in a_dictionary:
        if a_dictionary[keys] == value:
            key_del.append(keys)

    for words in key_del:
        del a_dictionary[words]

    return a_dictionary
