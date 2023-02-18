#!/usr/bin/python3
""" Module contain function which prints text """


def matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")

    arowlen = len(m_a[0])
    browlen = len(m_b[0])

    for row in m_a:
        if len(row) != arowlen:
            raise TypeError("each row of m_a must should be of the same size")
        for col in row:
            if isinstance(col, (float, int)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if len(row) != browlen:
            raise TypeError("each row of m_b must should be of the same size")
        for col in row:
            if isinstance(col, (float, int)):
                raise TypeError("m_b should contain only integers or floats")

    if arowlen != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    newmatrix = []
    for x in range(len(m_a)):
        newrow = []
        for y in range(browlen):
            sum = 0
            for z in range(arowlen):
                sum += m_a[x][z] * m_b[z][y]
            newrow.append(sum)
        newmatrix.append(newrow)
    return newmatrix
