#!/usr/bin/python3
"""
Function define check class
"""


def inherits_from(obj, a_class):
    """
    Check if object is an inherited instance of a class
    Arg:
        obj: the object to check
        a_class: Tte class
    Returns
        True or False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
