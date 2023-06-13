#!/usr/bin/python3
"""
Defines function that writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """
    initialise function
    Args:
        filename: name of the file to write
        text: string to write to the file
    Return:
        the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        charac = f.write(text)
    return charac
