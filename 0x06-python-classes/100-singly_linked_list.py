#!/usr/bin/python3
"""Module documents a class named Node """


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
        """Initialization of the dta node
        Args:
            data (int): data
            next_node: next_node
        Returns:
            None
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """The data property.
        Return:
            data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """sets the data into a node
        Args:
            value (int): data
        Raises:
            TypeError: if data is not int
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The next_node property.
        Return:
            next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next node
        Args:
            value: next_node
        Raises:
            TypeError: if next node is not node object
        Returns:
            None
        """
        if value is not None or not isinstance(value, list):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Class the defines a singly linked list
    Simple instantiation:
        -def __init__(self)
    Public instance method:
        -def sorted_insert(self, value)
    """
    def __init__(self):
        """Initialise class"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into the correct position"""
        NewNode = Node(value)
        temp = self.head
        if temp is None:
            self.head = Newnode
            return
        if value < temp.data:
            NewNode.next_node = self.head
            self.head = NewNode
            return

        while (temp.next_node and temp.next_node.data < value):
            temp = temp.next_node
        NewNode.next_node = temp.next_node
        temp.next_node = NewNode
