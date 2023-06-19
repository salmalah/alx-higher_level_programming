#!/usr/bin/python3
"""
define class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    Intialize Class constructor
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.x = x