#!/usr/bin/python3
"""Module containing Square class the inherits from Rectangle"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of Square class
        Args:
            size: size
            x: x
            y: y
            id: id
        Raises:
            None
        Returns:
            None
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".\
                format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """The size property."""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
