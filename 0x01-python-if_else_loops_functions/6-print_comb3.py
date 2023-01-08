#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if y < x or y == x:
            continue
        if (x != 8):
            print("{:d}{:d}".format(x, y), end=', ')
        else:
            print("{:d}{:d}".format(x, y))
