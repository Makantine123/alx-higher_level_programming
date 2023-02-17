#!/usr/bin/python3
"""Module defines function that divides all elements of matrix"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats") 
    if not (isinstance(div, float) or isinstance(div, int)):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    nmatrix = []
    for i in range(len(matrix[0])):
        for k in range(i):
            nmatrix[i][k] = round(matrix[i][k] / div, 2)
    return nmatrix
