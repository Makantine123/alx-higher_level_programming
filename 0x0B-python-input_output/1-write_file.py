#!/usr/bin/python3
""" Write string to text file """


def write_file(filename="", text=""):
    """Function writes text to a file """ 
    with open(filename, "w", encoding="utf-8") as myfile:
        myfile.write(text)
    return myfile
