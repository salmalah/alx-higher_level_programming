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
        with open(filename, "w") as jsfile:
            if list_objs is None:
                jsfile.write("[]")
            else:
                ls = [n.to_dictionary() for n in list_objs]
                jsfile.write(Base.to_json_string(ls))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
