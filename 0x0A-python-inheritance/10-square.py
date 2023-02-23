#!/usr/bin/python3
"""
Square Class inherits Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle

""" Program that creates a Square and instance its values """


class Square(Rectangle):
    """Class Rectangle, inherits from BaseGeometry"""
    def __init__(self, size):
        """ Initialization of rectangle class """
        self.__size = size
        Rectangle.integer_validator(self, "size", self.__size)

    def area(self):
        """ Area of square """
        return self.__square * self.__square
