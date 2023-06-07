#!/usr/bin/python3
"""
A function print a square with the character '#'
Arg:
    size: integer size length of the square
"""


def print_square(size):
    """
    Prints a square
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
