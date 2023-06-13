#!/usr/bin/python3
"""
Defines function append string at the end of a text
"""


def append_write(filename="", text=""):
    """
    Initialise funjction
    Args:
        filename: file to write in
        text: text to write in the end of file
    Return:
         the number of characters we aee
    """
    with open(filename, 'a', encoding="utf-8") as fi:
        n = fi.write(text)
    return n
