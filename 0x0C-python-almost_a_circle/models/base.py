#!/usr/bin/python3
""" Module """

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list_objs to a file
        Args:
            list_objs: List of an instance who inherits of Base
        """
        if list_objs is None:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filen = cls.__name__ + ".json"
        with open(filename, "w") as myfile:
            myfile.write(jstr)
