#!/usr/bin/python3
"""
Function found the max Integer in list
"""


def max_integer(list=[]):
    """
    found the max integer
    args:
       list: list of integer
    Return:
       Maximum integer in the list
       or None if the list is empty
    """
    if len(list) == 0:
        return None
    max_n = list[0]
    index = 1
    while index < len(list):
        if list[index] > max_n:
            max_n = list[index]
        index += 1
    return max_n
