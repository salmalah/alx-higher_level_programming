#!/usr/bin/python3
"""
a function that prints Full name
Args:
    first_name: The first name string
    last_name : The last name Defaults to an empty
                string is optional
"""


def say_my_name(first_name, last_name=""):
    """
    Initialize funtion that prints "My name is <first_name> <last_name>

    Raise:
        TypeError: If first_name / last_name is not a string

    Return:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))
