#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    unique_i = set()
    for n in my_list:
        unique_i.add(n)
        result = sum(unique_i)
    return result
