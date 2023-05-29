#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    coun = 0
    try:
        for index in range(x):
            print(my_list[index], end="")
            coun += 1
    except IndexError:
        pass
    print()
    return coun
