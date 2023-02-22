#!/usr/bin/python3
"""Module function"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance class that inhererited a_class
    """
    return (issubclass(obj, a_class))
