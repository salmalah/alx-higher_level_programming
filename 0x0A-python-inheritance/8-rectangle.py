#!/usr/bin/python3
"""
A class Rectangle that inherit fromm BaseGeometry
imprt the module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    initlise the class
    Args:
       width: width of the new Rectangle
       height: height of the new Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
