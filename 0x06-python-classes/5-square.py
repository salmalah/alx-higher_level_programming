#!/usr/bin/python3
"""
This class that defines a square

Attributes:
    private instance attribute: size

Methodes:
    __init__: Initializes a new instance of the Square class

    def area(self): returns the current square area


"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size : The size of the square

        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute

        returne the size of square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute

        Parameters:
        value: The size of the square

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints the square with the character #

        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__size):
                print("#" * self.__size)

    def area(self):
        """
        returns the area of the square

        None Parameters

        """
        return self.__size * self.__size
