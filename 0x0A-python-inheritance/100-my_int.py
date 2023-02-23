#!/usr/bin/python3
""" Module contains a MyInt class that inherits int """


class MyInt(int):
    """  Class MyInt inherits int """
    def __eq__(self, other):
        """ Equal Operator """
        if self == other:
            return False
        else:
            return True

    def __ne__(self, other):
        """ Not Equal Operator """
        if self != other:
            return False
        else:
            return True
