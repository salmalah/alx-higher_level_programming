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
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if dictionary != {} and dictionary:
            if cls.__name__ == "Rectangle":
                dm = cls(1, 1)
            else:
                dm = cls(1)
            dm.update(**dictionary)
            return dm

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

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                ls = Base.from_json_string(f.read())
                return [cls.create(**d) for d in ls]
        except FileNotFoundError:
            return []
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
