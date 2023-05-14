#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 934, 5, -13, 3]
list_l = [] 
max_value = max_integer(my_list)
max_v = max_integer(list_l)
print("Max: {}".format(max_value))
print("Max: {}".format(max_v))
