#!/usr/bin/python3
"""Module class Student"""

def __init__(self, first_name, last_name, age):
    """Initialization of Student class"""
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

def to_json(self):
    """Retrieves a dictionary representation of a Student instance
    (same as 8-class_to_json.py)"""
    resdict = {}
    objdict = self.__dict__
    for el in objdict:
        if type(objdict[el]) in [list, dict, str, int, bool]:
            resdict[el] = objdict[el]
    return resdict
