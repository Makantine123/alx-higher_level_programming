#!/usr/bin/python3
""" Append string to text file """


def append_write(filename="", text=""):
    """Function appends a string at the end of a text file"""
    with open(filename, "w", encoding="utf-8") as myfile:
        return myfile.write("\n" + text)
