#!/usr/bin/python3
""" Returns a python string representation of an json object """
import json


def from_json_string(my_str):
    """Returns string from json object"""
    return (json.loads(my_str))
