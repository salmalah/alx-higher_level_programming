#!/usr/bin/python3
"""
define student module
"""


class Student:
    """
    Initialise a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialises the attributes first_name/last_name/age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def reload_from_json(self, json):
        """
        method that replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary of a Student instance
        """
        if type(attrs) == list and all([type(n) == str for n in attrs]):
            return {key: value for key, value in vars(self).items()
                    if key in attrs}

        return vars(self)
