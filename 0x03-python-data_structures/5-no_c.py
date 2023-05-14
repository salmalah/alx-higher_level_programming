#!/usr/bin/env python3
def no_c(my_string):
    result = ""
    for c in my_string:
        if c not in ('c', 'C'):
            result += c
        return result
