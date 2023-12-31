#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list[:x]:
            if isinstance(i, int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
    except IndexError:
        print("IndexError: list  index out of range")

    return count
