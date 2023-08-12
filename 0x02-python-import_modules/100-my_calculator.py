#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    num = len(argv) - 1
    operator = ['+', '-', '*', '/']

    if num != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    expr = argv[2]

    if expr not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if expr == '+':
            print(f"{a} {expr} {b} = {add(a, b)}")
        elif expr == '-':
            print(f"{a} {expr} {b} = {sub(a, b)}")
        elif expr == '*':
            print(f"{a} {expr} {b} = {mul(a, b)}")
        else:
            print(f"{a} {expr} {b} = {div(a, b)}")
