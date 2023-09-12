#!/bin/usr/python3

""" This is a decription of this module .

This module contains a function called text_indentation
that checks for th valid given
datatypes and returns a sum of tow integer
style Guide`_. Docstrings may extend over
multiple lines. Sections are created
with a section header and a colon followed
by a block of indented text.
"""


def matrix_mul(m_a, m_b):
    """Class methods are similar to regular functions.
    Note:
        Do not include the `self` parameter in the ``Args`` section.
    Returns:
        returns 
    """
    m_c = []
    value = 0
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for i in range(len(m_a)):
        value = 0
        if not isinstance(m_a[i], list):
            raise TypeError("m_a must be a list of lists")
        for j in range(len(m_b)):
            if not isinstance(m_b[i], list):
                raise TypeError("m_b must be a list of lists")
            if not isinstance(m_a[i][j], int) and isinstance(m_a[i][j], float):
                raise TypeError("m_a should contain only integers or floats")
            if not isinstance(m_b[j][i], int) and isinstance(m_b[j][i], float):
                raise TypeError("m_b should contain only integers or floats")
            if len(m_a[i]) < 1 and len(m_a[i]) != len(m_b[j]):
                raise TypeError("each row of m_a must be of the same size")
            if len(m_b[j]) < 1 and len(m_a[i]) != len(m_b[j]):
                raise TypeError("each row of m_b must be of the same size")
            value += m_a[i][j] * m_b[j][i]
        m_c.append(value)

