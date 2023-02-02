#!/usr/bin/python3
"""Defines a class Square, based on 5-square.py"""


class Square:
    """Class square contains size, raises type and value errors, return area,
    has property, prints to the stdout with #"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area """
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

    def position(self):
        """The position property."""
        return self._position_position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def my_print(self):
        """Prints to standard output the square using # else and empty line"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print("_", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
