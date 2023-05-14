#!/usr/bin/python3
def no_c(my_string):
    table = {99: 0, 67: 0}
    new_str = my_string.translate(table)
    return new_str
