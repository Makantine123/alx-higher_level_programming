#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence <> "":
        strlen = len(sentence)
        firstChar = sentence[0]
    else:
        strlen = 0
        firstChar = None

    tupleR = (strlen, firstChar)
    return tupleR
