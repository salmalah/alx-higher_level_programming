#!/usr/bin/python3
"""
defines functions import json
"""
import json


def to_json_string(my_obj):
    """
    Initialise function
    Return:
         JSON representation of an string object
    """
    return json.dumps(my_obj)
