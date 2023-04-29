#!/usr/bin/python3
"""
Function finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Function finds a peak in a list"""

    if (len(list_of_integers) == 0):
        return None
    elif (len(list_of_integers) == 1):
        return list_of_integers[0]

    max = list_of_integers[0]

    for i in range(len(list_of_integers)):
        if list_of_integers[i] > max:
            max = list_of_integers[i]

    return max
