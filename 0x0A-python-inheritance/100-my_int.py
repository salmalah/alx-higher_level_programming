#!/usr/bin/python3
"""
module class Myint
"""


class MyInt(int):
    """
    A class representing a rebel integer
    Attributes:
        No additional attributes.

    Methods:
        __eq__(self, other): Overrides the == operator
        __ne__(self, other): Overrides the != operator
    """

    def __eq__(self, other):
        """
        Overrides the == operator

        Args:
            other: The value to compare
        Return:
            True if the values are not equal or flse
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator
        Arg:
            other: The value to compare with

        Return
            True if the values are equal,or False
        """
        return super().__eq__(other)
