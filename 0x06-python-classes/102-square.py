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

    def area(self):
        """
        returns the area of the square

        None Parameters

        """
        return self.__size * self.__size
    def __eq__(self, other):
        """
        Compares two squares if they are equqls
        """
        return self.area() == other.area()
    def __lt__(self, other):
        """
        check if the area of the current square is less than the area
        """
        return self.area() < other.area()
    def __le__(self, other):
        """
        check if the area of the current square is less than or equal the area
        """
        return self.area() <= other.area()
    def __ne__(self, other):
        """
        check two squares for inequality based on their areas
        """
        return self.area() != other.area()
    def __ge__(self, other):
        """
        check if the area of the current square is greater than or equal to the area
        """
        return self.area() >= other.area()
    def __gt__(self, other):
        """
        if the area of the current square is greater than the area
        """
        return self.area() > other.area()
