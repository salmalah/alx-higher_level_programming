#!/usr/bin/python3
"""
define function write an object to a text file using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    initalise function
    Args:
        my_obj: object to be saved to the file
        filename: The name of the file to write the JSON representation to
    Return:
        Nothing
    """
    with open(filename, 'w', encoding="utf-8") as fs:
        json.dump(my_obj, fs)
