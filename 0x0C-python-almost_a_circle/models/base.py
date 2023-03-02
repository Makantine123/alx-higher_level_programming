#!/usr/bin/python3
""" Module """
import os
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

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if (cls.__name__ == 'Rectangle'):
            dummy = cls(1, 1)
        elif (cls.__name__ == 'Square'):
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        mylist = []
        filename = cls.__name__ + '.json'
        if os.path.isfile(filename):
            with open(filename, "r") as myfile:
                stread = myfile.read()
                ljson = cls.from_json_string(stread)
                for i in ljson:
                    mylist.append(cls.create(**i))
        return (mylist)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs in csv format, save file"""
        if (not isinstance(list_objs, list) and list_objs is not None
        or all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        while open(filename, "w") as myfile:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(myfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from file, return list of instances"""
        filename = cls.__name__ + ".csv"
        mylist = []
        if os.path.exist(filename):
            with open(filename, "r") as myfile:
                reader = csv.reader(myfile, delimiter=", ")
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        mylist.append(i)
        return mylist
