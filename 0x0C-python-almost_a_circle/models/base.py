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
                ins = ins.to_dictionary()
                json_dict = json.loads(cls.to_json_string(ins))
                mylist.append(json_dict)
        with open(filename, "w") as f:
            json.dump(mylist, f)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = Rectangle(1, 1)
        elif cls.__name__ == 'Square':
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy
