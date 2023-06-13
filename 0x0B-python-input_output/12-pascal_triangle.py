#!/usr/bin/python3
"""
define a function Pascal"""


def pascal_triangle(n):
    """
    initalise function

    Return:
      list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) != n:
        t = tr[-1]
        tp = [1]
        for v in range(len(t) - 1):
            tmp.append(t[v] + t[v + 1])
        tp.append(1)
        tr.append(tp)
    return tr
