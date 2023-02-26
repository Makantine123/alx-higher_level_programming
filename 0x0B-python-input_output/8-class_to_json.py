#!/usr/bin/python3
"""
Function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for
JSON serialization of an object
"""


def class_to_json(obj):
    """Returns the dictionary description with data structure"""
    resdict = {}
    objdict = obj.__dict__
    for el in objdict:
        if type(objdict[el]) in [list, dict, str, int, bool]:
            resdict[el] = objdict[el]
    return resdict
