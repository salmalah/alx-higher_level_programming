#!/usr/bin/python3
"""
Represents a node of a singly linked list

Attribute:
    data : The data stored in the node
    next_node: The reference to the next node
"""


class Node:
    """
    initializes a new instance of the Node
    """
    def __init__(self, data, next_node=None):
        """Initializes the  a new instance of the Node class
        Return:
            None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        The data stored in the node
        return: The data value
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        setter sets the data stored in the node
        Raise:
        TypeError: If value is not an integer
        return None
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter reference to the next node in the list

        Return:
           Node: The next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter the reference to the next node in list

        Var:
            value: next node in the linked list
        Raise:
            TypeError: If value is not a Node object or None
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """String representation of Node instance

        Returns:
            Formatted string representing the node
        """
        return str(self.__data)


class SinglyLinkedList:
    """
    a singly linked list
    Attribute:
         head: The head of the linked list
    """
    def __init__(self):
        """
        initializes a new instance of the SinglyLinkedList class
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        inssert new Node into the correct sorted position

        Args:
            value : data stored inside the new node
        """
        new_n = Node(value)
        if self.__head is None or value < self.__head.data:
            new_n.next_node = self.__head
            self.__head = new_n
        else:
            currt = self.__head
            while currt.next_node is not None and currt.next_node.data < value:
                currt = currt.next_node
            new_n.next_node = currt.next_node
            currt.next_node = new_n

    def __str__(self):
        """
        resentation of SinglyLinkedList instance
        """
        out = ""
        self_h = self.__head
        while self_h is not None:
            out += str(self_h)
            if self_h.next_node is not None:
                out += "\n"
            self_h = self_h.next_node
        return out
