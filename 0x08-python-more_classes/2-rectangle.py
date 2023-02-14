#!/usr/bin/python3
"""Rectangle Class based on 1-rectangle.py"""


class Rectangle:
    """Defines a rectangle class"""
    def __init__(self, width=0, height=0):
        """
        Initialization of class object
        Args:
            width: Width of rectangle
            height: Height of rectangle
        Returns:
            Nothing
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter of a rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height property of a square"""
        return self.__height

    @height.setter
    def height(self, value):
        """The height setter of a rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))
