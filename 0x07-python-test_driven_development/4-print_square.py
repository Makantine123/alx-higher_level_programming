#!/usr/bin/python3
""" Module contains function that prints a square """


def print_square(size):
    """Function prints a square with character #"""
    if isinstance(size, float) and size < 0:
        raise TyepError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for k in range(size):
            print("#")
        print()
