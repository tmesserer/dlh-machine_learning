#!/usr/bin/env python3
"""Module for linear algebra"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates two matrices along an axis.
    Args:
        mat1: a list
        mat2: a list
        axis: integer"""
    new_mat = []
    new_row = []
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        for row in mat1:
            new_mat.append(row[:])
        for row in mat2:
            new_mat.append(row[:])
        return new_mat
    else:
        if len(mat1) != len(mat2):
            return None
        for i in range(0, len(mat1)):
            new_row.extend(mat1[i])
            new_row.extend(mat2[i])
            new_mat.append(new_row)
            new_row = []
        return new_mat
