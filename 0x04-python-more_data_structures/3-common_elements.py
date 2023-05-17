#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = set()
    for a in set_1:
        if a in set_2:
            set_3.add(a)
    return set_3
