#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for elemt in matrix:
        for a in range(len(elemt)):
            print('{:d}'.format(elemt[a]), end=(' ' * (a < len(elemt) - 1)))
        print()
