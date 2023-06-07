#!/usr/bin/python3
"""
a function that adds 2 integers
Argments:
    a : first number int or float
    b : second number default value is 98
"""


def add_integer(a, b=98):
    """
    Raise:
       TypeError: If value of  a or b is not an integer /float
    Return:
       The addition of a and b must be integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
