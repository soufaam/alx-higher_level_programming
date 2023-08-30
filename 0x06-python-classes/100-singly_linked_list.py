#!/usr/bin/python3

""" This is a decription of this module .

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.
"""


class Node:
    """A class Node that defines a node of a singly linked list by:
    """
    def __init__(self, data=0, next_node=None):
        """
         The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
        Args:
            data (int): integer var.
            next (Node): the node
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node
    """  Attributes:
        __data:  must be an integer, otherwise raise a TypeError exception
        with the message data must be an integer
        __next_node:next_node can be None or must be a Node, otherwise raise
        a TypeError exception with the message
        next_node must be a Node object"""

    @property
    def data(self):
        """property def data(self): to retrieve it"""
        return self.__data

    @data.setter
    def data(self, value):
        """property setter def data(self, value): to set it
        Args:
            value (int): set the __data to value.
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """property def next_node(self): to retrieve it
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property setter def next_node(self, value): to set it
        Args:
            value (int): set the __postion to value.
        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
        return self.__next_node


class SinglyLinkedList:
    """a class SinglyLinkedList that defines a singly linked list"""
    def __init__(self, head=None) -> None:
        """Simple instantiation: def __init__(self):"""
        self.__head = head
        """ Attributes:
        __head: Private instance attribute: head (no setter or getter)"""
    def sorted_insert(self, value):
        """Public instance method: def sorted_insert(self, value):
        that inserts a new Node into the correct sorted position in
        the list (increasing order)"""
        node = Node(value, None)
        tmp = self.__head
        prev = self.__head
        if self.__head is None:
            node.next_node = None
            self.__head = node
            return self.__head
        if self.__head.data >= node.data:
            node.next_node = self.__head
            self.__head = node
            return self.__head
        while (tmp is not None):
            if node.data <= tmp.data:
                node.next_node = tmp
                prev.next_node = node
                break
            elif node.data > tmp.data and tmp.next_node is None:
                tmp.next_node = node
                node.next_node = None
                break
            prev = tmp
            tmp = tmp.next_node
        return self.__head

    def __str__(self) -> None:
        """_str__ make the singly_linked_list printable:
        =>print the entire list in stdout
        =>one node number by line"""
        tmpnode = self.__head
        flag = False
        while tmpnode is not None:
            if not tmpnode.next_node:
                flag = True
                break
            print(f"{tmpnode.data}")
            tmpnode = tmpnode.next_node
        if flag:
            print(f"{tmpnode.data}", end='')
        return ''
