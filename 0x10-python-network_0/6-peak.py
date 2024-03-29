#!/usr/bin/python3
"""
Function finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Function to find a peak in a list"""
    if list_of_integers == []:
        return None
    ll = len(list_of_integers)
    m = ll // 2
    arr = list_of_integers
    while True:
        if m in (0, ll - 1) or arr[m - 1] < arr[m] > arr[m + 1]:
            return arr[m]
        if arr[m] < arr[m + 1]:
            m = (ll + m) // 2
        else:
            m = m // 2
