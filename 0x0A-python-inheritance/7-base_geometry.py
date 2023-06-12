#!/usr/bin/python3
"""
module an empty class
"""


class BaseGeometry:
    """
    define the empty class
    method:
       Public instance method: def area(self)
       def integer_validator(self, name, value)
    """
    def area(self):
        """
        impelement method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Raisers:
            if value is not an integer
            if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
