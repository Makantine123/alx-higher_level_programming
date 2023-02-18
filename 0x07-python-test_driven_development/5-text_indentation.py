#!/usr/bin/python3
""" Module contain function which prints text """


def text_indentation(text):
    """
    Function prints a text with 2 new lines after each of these characters
    . , ? , :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0

    for i in range(len(text)):
        if flag == 1:
            if text[i + 1] != " " and i < len(text):
                flag = 0
            continue
        if text[i] in [".", "?", ":"]:
            print(text[i], end="")
            print("")
            print("")
            if text[i + 1] == " " and i < len(text):
                flag = 1
        else:
            print(text[i], end="")