#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    newl = my_list
    if idx < 0:
        return newl
    elif idx > len(newl) - 1:
        return newl
    else:
        newl[idx] = element
        return newl
