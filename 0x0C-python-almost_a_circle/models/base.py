#!/usr/bin/python3
"""
define a class Base"
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
