#!/usr/bin/python3
"""
MagicClass that does exactly the same as the following Python bytecode

"""
import math


class MagicClass:
    """
    This class that represents a circle and provides various calculation
    """
    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance
        Var:
          radius: The radius of the circle
        Raises:
           TypeError: f the radius is not a number
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle
        Return: The area of the circle

        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle
        Return: The circumference of the circle
        """
        return 2 * math.pi * self.__radius
