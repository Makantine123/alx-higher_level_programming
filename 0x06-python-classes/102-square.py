#!/usr/bin/python3
"""Defines a class Square, based on 4-square.py"""


class Square:
    """Class square contains size, raises type and value errors, return area,
    has property"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of a square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Equal to comparison"""
        return self.area() == other.area()

    def __nteq__(self, other):
        """Not Equal to comparison"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison"""
        return self.area() > other.area()

    def __gteq__(self, other):
        """Greater than equal too comparison"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparison"""
        return self.area() < other.area()

    def __lteq__(self, other):
        """Less than equal too comparison"""
        return self.area() <= other.area()
