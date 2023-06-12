#!/usr/bin/python3
"""
Function adds attributes to an object
"""


def add_attribute(obj, name, value):
    """
    Intialise functions
    Adds attributes
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
