#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
Attributes:
    __width: The width of the rectangle
    __heigh: The height of the rectangle
Methodes:
    __init__: Initializes a new instance of the rectangle
"""

class Rectangle:
    """
    Defines Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width: Defaults to 0.
            height: Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width of the rectangle.

        Returns:
            the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width

        Args:
            value: integer value of the width of the rectangle

        Raises:
            TypeError: if is not an integer
            ValueError: if the width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height

        Return:
            the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle

        Args:
            value: integer

        Raises:
            TypeError: If is not an integer.
            ValueError: If the height < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

