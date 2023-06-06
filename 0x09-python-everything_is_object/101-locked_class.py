#!/usr/bin/python3
"""
A class LockedClass with no object
Attribute:
    No
"""


class LockedClass:
    """creating new instance attributes
    except if the new instance attribute is called first_name
    """
    __slots__ = ['first_name']
