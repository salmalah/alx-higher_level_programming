#!/usr/bin/python3
"""
A module Mylist inherits from list
"""


class MyList(list):
    """
    Implement the class
    """

    def print_sorted(self):
        """
        Function Print sorted ascending order list"""
        print(sorted(self))
