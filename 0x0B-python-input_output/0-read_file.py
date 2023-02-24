#!/usr/bin/python3
""" Read a text file """


def read_file(filename=""):
    """Function reads file name """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
