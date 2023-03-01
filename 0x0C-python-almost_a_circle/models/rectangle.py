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
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The height property."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The x property."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The y property."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Are of rectangle"""
        return (self.width * self.height)

    def display(self):
        """Prints instance with the character #"""
        wd = self.width
        ht = self.height

        for y in range(self.y):
            print()
        for h in range(ht):
            print(" " * self.x, end="")
            print("#" * wd)

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".\
                format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to attributes
        Args:
            id: id , 1st argument
            width: width, 2nd argument
            height: height, 3rd argument
            x: x, 4th argument
            y: y, 5th argument
        """
        if len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                exec("self.{} = {}".format(key, value))
