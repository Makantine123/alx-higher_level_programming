#!/usr/bin/python3
"""
Square Class: defines a square by : (based on 2-square.py)
"""


class Square:
    """ class Square that defines a square """
    def __init__(self, size=0):
        """ Initialize attributes"""
        self.size = size

    @property
    def size(self):
        """ gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size with safe Assignment"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Return the area of the square"""
        return (self.__size * self.__size)

    def __lt__(self, other):
        """ less than comparison """
        return self.area() < other.area()

    def __le__(self, other):
        """ less than or equal than comparison """
        return self.area() <= other.area()

    def __eq__(self, other):
        """ equal to comparison """
        return self.area() == other.area()

    def __ne__(self, other):
        """ not equal comparison """
        return self.area() != other.area()

    def __gt__(self, other):
        """ greater than """
        return self.area() > other.area()

    def __ge__(self, other):
        """ greater than or equal to """
        return self.area() >= other.area()
