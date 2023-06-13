#!/usr/bin/python3
"""
define a class student
"""


class Student:
    """
    Initialise student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialises first_name/last_name/age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary of a Student instance
        """
        return vars(self)
