#!/usr/bin/python3
""" Writes an object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """Writes object to to text file"""
    with open(filename, "w") as myfile:
        json.dump(my_obj)
