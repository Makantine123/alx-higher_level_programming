#!/usr/bin/python3
""" Module """


class Base:
    """ Base class, is the base of all other classess in project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of base class
        Args:
            id: id of instance
        Raises:
            None
        Return:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
