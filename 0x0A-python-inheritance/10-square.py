#!/usr/bin/python3
"""
module Square that inherits fromm Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Initialise the class Square that inherits frm area
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        define area
        """
        return (self.__size * self.__size)
