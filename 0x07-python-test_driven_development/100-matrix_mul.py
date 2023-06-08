#!/usr/bin/python3
"""
Function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices
    Args:
        m_a: The first matrix for int/integers numbers
        m_b: The second matrix of int/float numbers
    Raises:
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
        TypeError: If empty m_a or m_b
    Return:
        new matrix multiple of m_a by m_b.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    l2 = None
    for r in m_a:
        if type(r) is not list:
            raise TypeError("m_a must be a list of lists")
        if l2 is None:
            l2 = len(r)
            if l2 == 0:
                raise ValueError("m_a can't be empty")
        if l2 != len(r):
            raise TypeError("each row of m_a must should be of the same size")
        for elem in r:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    l3 = None
    for r in m_b:
        if type(r) is not list:
            raise TypeError("m_b must be a list of lists")
        if l3 is None:
            l3 = len(r)
            if l3 == 0:
                raise ValueError("m_b can't be empty")
        if l3 != len(r):
            raise TypeError("each row of m_b must should be of the same size")
        for e in r:
            if type(e) is not int and type(e) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if l2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matr = []
    for ind in range(len(m_a)):
        ls = []
        for j in range(l3):
            n = 0
            for k in range(l2):
                n += m_a[ind][k] * m_b[k][j]
            ls.append(n)
        matr.append(ls)
    return matr
