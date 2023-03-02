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
        mylist = []
        filename = cls.__name__ + '.json'
        if (list_objs is not None):
            for ins in list_objs:
                my_list.append(ins.to_dictionary())
        jstr = cls.to_json_string(my_list)
        with open(filename, "w") as myfile:
            myfile.write(jstr)
