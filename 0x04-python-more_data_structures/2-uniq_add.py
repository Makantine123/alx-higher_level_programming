#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    for val in set(my_list):
        result += val
    return (result)
