#!/usr/bin/python3
"""
Module contains function that returns true if object is exactly an instance
of the specified class. otherwise False
"""

def is_same_class(obj, a_class):
    """function returns True if object is an instance of class"""
    if type(obj) == a_class:
        return True
    return False
