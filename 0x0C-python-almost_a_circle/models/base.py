#!/usr/bin/python3
"""
define a class Base"
"""


class Base:
    """
    Base class
    declare the private attribute
    """
    __nb_objects = 0
    """
    Initializes a new instance
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
