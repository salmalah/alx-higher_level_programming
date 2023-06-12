#!/usr/bin/python3
"""
Moule Square that inherits fromm Rectangle
"""
Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """
    Initialise class Square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        define function are
        Return:
            the area of the square
            """
        return (self.__size * self.__size)

    def __str__(self):
        """
        define function str
        return:
            description of the square
        """
        str_rep = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return str_rep
