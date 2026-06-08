#!/usr/bin/env python3
"""Module for linear algebra"""


def mat_mul(mat1, mat2):
    """multiplies two matrices.
    Args:
        mat1: a list
        mat2: a list
    """
    if len(mat1[0]) != len(mat2):
        return None
    if any(len(row) != len(mat1[0]) for row in mat1):
        return None
    if any(len(row) != len(mat2[0]) for row in mat2):
        return None
    new_element = 0
    new_row = []
    new_matrix = []
    for row1 in range(0, len(mat1)):
        for col2 in range(0, len(mat2[0])):
            for element in range(0, len(mat1[0])):
                new_element += mat1[row1][element] * mat2[element][col2]
            new_row.append(new_element)
            new_element = 0
        new_matrix.append(new_row)
        new_row = []
    return new_matrix
