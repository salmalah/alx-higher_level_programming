#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list) != 0:
        score, val = 0, 0
        for n in my_list:
            score += n[0] * n[1]
            val += n[1]
        return (score / val)
    else:
        return 0
