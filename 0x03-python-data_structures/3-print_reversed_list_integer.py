#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_r = my_list[::-1]
    for i in list_r:
        print("{:d}".format(i))
