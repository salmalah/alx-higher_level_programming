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
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square
        Raises:
            TypeError: If `size` is not an integer
            ValueError: if size is less than 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
