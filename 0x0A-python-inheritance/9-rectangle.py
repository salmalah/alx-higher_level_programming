#!/usr/bin/python3
"""
module Rectangle that inherits frommm BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class rectangle that inherits frm BaseGeometry
    """
    def __init__(self, width, height):
        """
        initializes Rectangle
        args:
            width
            height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """
        define str function
        Return:
           description of the Rectangle
        """
        str_dsc = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return str_dsc

    def area(self):
        """
        define function area of rectangle
        Return:
             area
        """
        return (self.__width * self.__height)
