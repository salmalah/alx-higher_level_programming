#!/usr/bin/python3
"""
a function that multiplies 2 matrices by using the module NumPy
"""
import numpy as n


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy
    Args:
        m_b: Second matrix represented as a list of lists
        m_a: First list of lists
    Returns:
        multiple of matrix
    """
    return (n.matmul(m_a, m_b))
