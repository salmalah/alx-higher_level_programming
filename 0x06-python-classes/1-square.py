#!/usr/bin/python3
"""
This class that defines a square

Attributes:
    private instance attribute: size

Methodes:
    __init__: Initializes a new instance of the Square class


"""


class Square:
    """Defines a square"""
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square

        """
        self.__size = size
