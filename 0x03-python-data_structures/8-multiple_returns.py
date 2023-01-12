#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence > 0):
        strlen = len(sentence)
        firstChar = sentence[0]
    else:
        strlen = 0
        firstChar = None
    tupleR = (strlen, firstChar)
    return tupleR
