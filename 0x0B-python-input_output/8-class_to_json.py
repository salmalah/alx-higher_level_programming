#!/usr/bin/python3
"""
define function return the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Initialise function
    Arg:
        obj: an instance of a Class
    Return:
       the dictionary
    """
    return vars(obj)
