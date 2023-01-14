#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary == {} or a_dictionary is None):
        return (None)
    else:
        max_value = max(a_dictionary, key=a_dictionary.get)
        return max_value
