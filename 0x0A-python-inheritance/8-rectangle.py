#!/usr/bin/python3
"""
Rectangle Class inherits BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

""" Program that creates a Rectangle and instance its values """

class Rectangle(BaseGeometry):
    """Class Rectangle, inherits from BaseGeometry"""
    def __init__(self, width, height):
        """ Initialization of rectangle class """
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
        self.__width = width
        self.__height = height
