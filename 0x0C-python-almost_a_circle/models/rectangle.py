#!/usr/bin/python3
"""Rectangle Module, inherits from Base"""


Base = __import__("base.py").Base

""" Base Class from base.py """


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
