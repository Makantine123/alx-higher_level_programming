#!/usr/bin/python3
""" Module contains function that prints a square """


def print_square(size=10):
    """Function prints a square with character #"""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for k in range(0, size):
            if k != size - 1:
                print("#", end="")
            else:
                print("#")
