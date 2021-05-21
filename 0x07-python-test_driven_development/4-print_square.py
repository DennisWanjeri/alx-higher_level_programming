#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """prints a square with character '#'"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif (size < 0) is True:
        raise ValueError("size must be >= 0")
    elif type(size) is float and (size < 0) is True:
        raise TypeError("size must be an integer")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
