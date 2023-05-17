#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        found_v = [k for k, v in a_dictionary.items() if v == value]
        for v_d in found_v:
            del a_dictionary[v_d]
    return a_dictionary
