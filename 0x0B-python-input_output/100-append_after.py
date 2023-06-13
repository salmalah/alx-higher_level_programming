#!/usr/bin/python3
"""
define module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Initialise function insert a line of text to a file
    """
    content = ""
    with open(filename, "r", encoding="utf-8") as fs:
        for ln in fs:
            content += ln
            if search_string in ln:
                content += new_string
    with open(filename, "w", encoding="utf-8") as fb:
        fb.write(content)
