#!/usr/bin/python3
"""
deinfe function that returns an object
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """initialise function
    return:
        an object represented by a JSON
    """
    return json.loads(my_str)
