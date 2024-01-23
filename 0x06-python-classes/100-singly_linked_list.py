#!/usr/bin/python3
"""Define  a singly-linkedlist."""


class Node:
    """Represents a node in singly-linkedlist."""

    def __init__(self, data, next_node=None):
        """Initialize the new Node.

        Args:
            data (int): The data of  new Node.
            next_node (Node):  next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get || set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("the data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get || set the next_node of  Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents the singly-linked list."""

    def __init__(self):
        """Initialize  new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node in SinglyLinkedList.

        The node is inserted into the list at the exact
        ordered position.

        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Define  string representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(values)
