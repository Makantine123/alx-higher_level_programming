#!/usr/bin/python3
"""Module function"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance class that inhererited a_class
    """
    if (type(obj) == a_class):
        return False
    return (isinstance(obj, a_class))
