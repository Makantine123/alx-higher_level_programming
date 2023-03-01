#!/usr/bin/python3
"""Rectangle Module, inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of Rectangle class
        Args:
            width: Width of rectangle
            height: Height of rectangle
            x: x
            y: y
            id: id
        Raises:
            None
        Returns:
            None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """The width property."""
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        """The height property."""
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def x(self):
        """The x property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        """The y property."""
        return self._y
    @y.setter
    def y(self, value):
        self._y = value
