#!/usr/bin/python3
"""Module soles the nqueens problem"""


import sys


def nqueens(size):
    """Initial startup before backtracking algorithm"""
    if type(size) is not int:
        raise TypeError("N must be a number")
    if size < 4:
        raise ValueError("N must be at least 4")
    queens = [0] * size

def printqueens(queens):
    """Print a display of the queens"""
    print("[[0, ", queens[0], "]", sep="", end="")
    for y, x in enumerate(queens[0:], 1):
          print(", [", y, ", ", x, "]", sep="", end="")
    print("]")

def calcs(queen):
    """Recursive call queen position validator"""
    for x in range(size):
        """x position of queen"""
        next_x = 0
        for y in range(queen):
            qx = queens[y]
            if x ==qx or x + queen == qx + y or x - queen == qx - y:
                next_x = 1
                break
            if next_x == 1:
                next_x == 0
                continue
            if queen != size - 1:
                queens[queen + 1] = 0
                queens[queen] = x
                calcs(queen + 1)
            else:
                queens[queen] = x
                printqueens(queens)
    calcs(0)

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit()
try:
    size = int(sys.argv[1])
except (ValueErr, TypeError):
    print("N must be a number")
    exit()
nqueens(size)
