#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after each of these
characters: ., ? and :
"""


def text_indentation(text):
    """
    Print text

    Arg:
        text: The string value to print.
    Raise:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    coun = 0
    while coun < len(text) and text[coun] == ' ':
        coun += 1

    while coun < len(text):
        print(text[coun], end="")
        if text[coun] == "\n" or text[coun] in ":.?":
            if text[coun] in ".?:":
                print("\n")
            coun += 1
            while coun < len(text) and text[coun] == ' ':
                coun += 1
            continue
        coun += 1
