#!/usr/bin/python3
""" Module Function """


def is_kind_of_class(obj, a_class):
    """Returns True if obj is instance of inherited class from a_class"""
    if isinstance(obj, a_class):
        return True
    return False
