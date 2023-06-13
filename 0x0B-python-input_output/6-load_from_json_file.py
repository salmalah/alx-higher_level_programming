#!/usr/bin/python3
"""
define function creat an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    intialise function
    Args:
        filename: name of the JSON file to load the object from
    Return:
         object loaded from the JSON file
    """
    with open(filename, "r", encoding="utf-8") as fs:
        ob = json.load(fs)
    return ob
