#!/usr/bin/python3
def no_c(my_string):
    table = {99: None, 67: None}
    new_str = my_string.translate(table)
    return new_str
