#!/usr/bin/python3
"""
Function finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Function finds a peak in a list"""

    if (list_of_integers == []):
        return None

    max = list_of_integers[0]

    for i in range(len(list_of_integers)):
        if list_of_integers[i] > max:
            max = list_of_integers[i]

    return max
