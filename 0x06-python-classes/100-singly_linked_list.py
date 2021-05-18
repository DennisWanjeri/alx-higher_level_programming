#!/usr/bin/python3
"""singly linked list class"""


class Node:
    """class Node"""
    def __init__(self, data, next_node=None):
        """initialization"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """returns the value of data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """retrieves next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """next_node validation and setting"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """singlyLinkedList class"""
    def __init__(self):
        """class initialization"""
        self.__head = None
