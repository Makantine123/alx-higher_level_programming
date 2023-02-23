#!/usr/bin/python3
"""Rectangle Class inherits BaseGeometry"""


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """ Initialization of rectangle class """
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
        self.__width = width
        self.__height = height
