#!/usr/bin/python3
"""
Function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a: The first matrix for int/integers numbers
        m_b: The second matrix of int/float numbers
    Raises:
        TypeError: If m_a or m_b is not a list of int/ float list
        TypeError: If empty m_a or m_b
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Return:
        new matrix multiple of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not all(isinstance(r, list) for r in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(r, list) for r in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all((isinstance(e, float) or isinstance(e, int))
               for e in [n for row in m_b for n in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [n for r in m_a for n in r]):
        raise TypeError("m_a should contain only integers or floats")

    if not all(len(r) == len(m_b[0]) for r in m_b):
        raise TypeError("each row of m_b must should be of the same size")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for f in range(len(m_b[0])):
        new_r = []
        for c in range(len(m_b)):
            new_r.append(m_b[c][f])
        inverted_b.append(new_r)

    new_m = []
    for r in m_a:
        new_r = []
        for c in inverted_b:
            produit = 0
            for i in range(len(inverted_b[0])):
                produit += r[i] * c[i]
            new_r.append(produit)
        new_m.append(new_r)

    return new_m
