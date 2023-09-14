#!/usr/bin/python3
""" This module return the lists of integers """


def pascal_triangle(n):
    """This fuction return the lists of integers """
    if n <= 0:
        return []

    list_i = []
    for line in range(1, n + 1):
        P = 1
        row = []
        for i in range(1, line + 1):
            row.append(P)
            P = P * (line - i) // i
        list_i.append(row)
    return list_i
