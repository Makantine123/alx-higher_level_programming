#!/usr/bin/python3
"""
Square Class: Printing a square with # and coordinates
"""


class Square:
    """ class Square that defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize attributes"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ retrieve the initial potition """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the new position """
        s = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(s)
        elif (len(value) != 2):
            raise TypeError(s)
        else:
            for t in value:
                if (t < 0) or type(t) is not int:
                    raise TypeError(s)
                elif (type(t) is not int):
                    raise TypeError(S)
        self.__position = value

    def area(self):
        """ Return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """ prints in stdout the square with the character # """
        if (self.size != 0):
            for n in range(self.__position[1]):
                print("")
            for x in range(self.__size):
                for y in range(self.__size + self.__position[0]):
                    if (y < self.__position[0]):
                        print(" ", end="")
                    else:
                        print("#", end='')
                print('')
        else:
            print('')
