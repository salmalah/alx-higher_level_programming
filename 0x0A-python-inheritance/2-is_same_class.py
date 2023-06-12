#!/usr/bin/python3
"""
A Function check if objet is instance
"""


def is_same_class(obj, a_class):
    """
    Initialise function

    Args:
        obj: object to check
        a_class: class to match the type of obj to
    Return:
         True or False if is no instance objet
    """
    if type(obj) == a_class:
        return True
    return False
