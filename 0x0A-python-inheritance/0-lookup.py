#!/usr/bin/python3
"""
This module return the list of available attributes
and methods of an object
"""
def lookup(obj):
    """
    Function return list of  attributes/methods of an object
    Args:
       obj: objet
    Return: list
    """
    return dir(obj)
