#!/usr/bin/python3
"""Module class Student"""

def __init__(self, first_name, last_name, age):
    """Initialization of Student class"""
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

def to_json(self, atts=None):
    """
    Retrieves a dictionary representation of a Student instance
    (same as 8-class_to_json.py)
    """
    resdict = dict()
    if type(atts) is list:
        for x in atts:
            if x in self.__dict__:
                resdict.update({x: self.__dict__[x]})
        return resdict
    return self.__dict__.copy()
