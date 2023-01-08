#!/usr/bin/python3

def uppercase(str):
    for i in range(0, len(str)):
        letter = str[i]
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end='')
    print('')
