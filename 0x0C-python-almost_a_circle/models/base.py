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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        ls = []
        if list_objs is not None:
            ls = [ob.to_dictionary() for ob in list_objs]
        ls = cls.to_json_string(json_list)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
