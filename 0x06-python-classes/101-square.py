#!/usr/bin/python3
"""
This class defines a square
Attributes:
    __size: private instance attribute
    __position: private instance attribute

Methodes:
    area: Calculates and returns the area of the square
    size : Getter and setter for the size attribute
    my_print: Prints the square with the character #
    position : Getter and setter for the position attribut
    __init__:  Initializes a new instance of the Square class
"""


class Square:
    """Defines the square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Creates  a new instance of the Square class
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute

        Raises:
           TypeError: If the value is not an integer.
           ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter for the position attribut
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribut
        Raisers:
            TypeError: if not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        display area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character #
        prints an empty line if the size is equal = 0
        """
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for s in range(self.__size):
                print(" " * self.position[0] + "#" * self.size, end="")
                print()

    def __str__(self):
        """
        represent the Square instance
        """
        out = ""
        if self.size == 0:
            return out
        else:
            row = (" " * self.position[0] + "#" * self.size + "\n")
            output = "\n" * self.position[1] + row * self.size
        return output[:-1]
