#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l = sorted(a_dictionary.keys())
    for n in l:
        value = a_dictionary[n]
        print("{}: {}".format(n, value))
