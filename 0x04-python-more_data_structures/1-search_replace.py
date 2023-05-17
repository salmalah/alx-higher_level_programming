#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ne_l = []
    for n in my_list:
        if n == search:
            ne_l.append(replace)
        else:
            ne_l.append(n)
    return ne_l
