#!/usr/bin/python3
"""Defines a singly linked list."""


class Node:
    """Represents a Node of a singly linked list."""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value == None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")



class SinglyLinkedList:
    """Represents a singly linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        printed = ""
        node = self.head
        while node:
            printed += str(node.data) + '\n'
            node = node.next_node
        return printed[:-1]

    def sorted_insert(self, value):
        new = Node(value)
        if self.head != None:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        temp = self.head
        while temp.next_node and temp.next_node.data < value:
            temp = temp.next_node
        if temp.next_node:
            new.next_node = temp.next_node
        temp.next_node = new
