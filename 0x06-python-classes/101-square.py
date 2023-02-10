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
                if type(t) is not int:
                    raise TypeError(s)
                elif t < 0:
                    raise TypeError(s)
        self.__position = value

    def area(self):
        """ Return the area of the square"""
        return (self.__size * self.__size)

    def return_square(self):
        """ Returns the square to print function"""
        if (self.size != 0):
            sqstr = ""
            for n in range(self.__position[1]):
                sqstr += "\n"
            for x in range(self.__size):
                for y in range(self.__size + self.__position[0]):
                    if (y < self.__position[0]):
                        sqstr += " "
                    else:
                        sqstr += "#"
                sqstr += "\n"
            return sqstr
        else:
            sqstr += "\n"
            return sqstr

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
