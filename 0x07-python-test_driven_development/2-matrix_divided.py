#!/usr/bin/python3
"""Module defines function that divides all elements of matrix"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""
    matrixmsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(matrixmsg)
    if not (isinstance(div, float) or isinstance(div, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    nmatrix = []
    for i in range(len(matrix[0])):
        for k in range(i):
            if not isinstance(matrix[i][k], list):
            raise TypeError(matrixmsg)
            nmatrix[i][k] = round(matrix[i][k] / div, 2)
    return nmatrix
