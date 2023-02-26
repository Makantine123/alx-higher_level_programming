#!/usr/bin/python3
"""
Script that loads, adds and save all arguments to a Python list
,then saves them to a file
"""
import sys
savefile = __import__("5-save_to_json_file.py").save_to_json_file
loadfile = __import__("6-load_from_json_file.py").load_from_json_file


try:
    listn = loadfile("add_item.json")
except FileNotFoundError:
    listn = []
for i in sys.argv[1]:
    listn.append(i)
savefile(listn, "add_item.json")
