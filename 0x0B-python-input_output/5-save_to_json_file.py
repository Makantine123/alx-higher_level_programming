#!/usr/bin/python3
""" Writes an object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """Writes object to to text file"""
    return (json.dump(my_obj))
