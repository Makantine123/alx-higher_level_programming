#!/usr/bin/python3
"""Module defines function that divides all elements of matrix"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""
    matrixmsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(matrixmsg)
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    nmatrix = []
    rowlen = len(matrix[0])
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(matrixmsg)
        if len(i) != rowlen:
            raise TypeError("Each row of the matrix must have the same size")
        newrow = []
        for k in i:
            if not isinstance(k, (float, int)):
                raise TypeError(matrixmsg)
            newrow.append(round(float(k / div), 2))
        nmatrix.append(newrow)
    return nmatrix
