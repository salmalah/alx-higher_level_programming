#!/usr/bin/python3
"""
module class Myint
"""


class MyInt(int):
    """
    A class representing a rebel integer
    """
    def __eq__(self, other):
        """
        Overrides the == operator
        Return:
            True if the values are not equal or flse
        """
        return (super().__ne__(other))

    def __ne__(self, other):
        """
        Overrides the != operator
        Return
            True if the values are equal,or False
        """
        return (super().__eq__(other))
