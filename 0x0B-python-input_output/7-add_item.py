#!/usr/bin/python3
"""Script that loads, adds and save all arguments to a Python list
, then saves them to a file"""
import sys
import os


save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file

if __name__ == "__main__":
    data = "add_item.json"

    if os.path.isfile(data):
        my_list = load_from_json_file(data)
    else:
        my_list = []

    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, data)
