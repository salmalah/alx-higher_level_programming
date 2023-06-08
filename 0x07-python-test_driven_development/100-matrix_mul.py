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
    l1 = len(m_a)
    if l1 == 0:
        raise ValueError("m_a can't be empty")
    l2 = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if l2 is None:
            l2 = len(i)
            if l2 == 0:
                raise ValueError("m_a can't be empty")
        if l2 != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        #for j in i:
            #if not (isinstance(j, (int, float))):
                #if type(elem) is not int and type(elem) is not float:
                #raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
            for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    l3 = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if l3 is None:
            l3 = len(i)
            if l3 == 0:
                raise ValueError("m_b can't be empty")
        if l3 != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if l2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(l1):
        ls = []
        for j in range(l3):
            n = 0
            for k in range(l2):
                n += m_a[i][k] * m_b[k][j]
            ls.append(n)
        matrix.append(ls)
    return matrix
