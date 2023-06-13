#!/usr/bin/python3
"""
defines function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Initialise function
    Arg:
       filename: name of the file to read
    Return : Nothing
    """
    with open(filename, encoding='utf-8') as file:
        for w in file:
            print(w, end='')
