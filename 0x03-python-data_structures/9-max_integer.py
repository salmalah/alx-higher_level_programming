#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_number = 0
        for n in my_list:
            if n > max_number:
                max_number = n
        return max_number
