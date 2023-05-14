#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for n in my_list:
        if n % 2 == 0:
            n = True
            new_list.append(n)
        else: 
            n = False
            new_list.append(n)
    return new_list
