#!/usr/bin/python3
""" Module contains function that prints name """


def say_my_name(fist_name, last_name=""):
    """ Function Prints name 
        Args:
            fist_name: fisrt name
            last_name: last_name
        Raises:
            TypeError: fist name or last name must be strings
    """
    if not isinstance(first_name, str):
        raise TypeError("fisrt_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a sting")

    print("My name is {:s} {:s}".format(fisrt_name, last_name))
