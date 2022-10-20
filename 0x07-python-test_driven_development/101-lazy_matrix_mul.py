#!/usr/bin/python3

"""
Module contains function lazy_matrix_mul()
that uses NumPy to multiply 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply matrices using
    NumPy module
    """
    return np.matmul(m_a, m_b)
