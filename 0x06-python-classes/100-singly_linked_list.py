#!/usr/bin/python3
"""Module defines a class Node"""

class Node:
""" Defines a class node of a singly linked list
        - def __init__(self, data, next_node=None)
    Private instance attribute data:
        -def data(self)
        -def data(self, value)
        -value must be int else raise TypError
    Private instance attribute next_node:
        -def next_node(self)
        -def next_node(self, value)
        -value can be node or None else raise TypeError

    """

    def __init__(self, data, next_node=None):
        """Initialization of the dta node"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if next_node is not None or not isinstance(next_node, list):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """The data property."""
        return self._data
    @data.setter
    def data(self, value):
        """sets the data into a node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """The next_node property."""
        return self._next_node
    @next_node.setter
    def next_node(self, value):
        """sets the next node"""
        if value is not None or not isinstance(value, list):
            raise TypeError("next_node must be a Node object")
        self._next_node = value
