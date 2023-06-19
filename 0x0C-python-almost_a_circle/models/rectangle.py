#!/usr/bin/python3
"""
define class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Intialize Class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """
        Getter method for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute
        """
        self.__height = value

    @property
    def width(self):
        """
        Getter method for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute
        """
        self.__width = value

    @property
    def y(self):
        """
        Getter method for the y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute
        """
        self.__y = value

    @property
    def x(self):
        """
        Getter method for the x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute
        """
        self.__x = value
