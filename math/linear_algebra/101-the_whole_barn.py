#!/usr/bin/env python3
"""Module for linear algebra"""


def add_matrices(mat1, mat2):
    """Element-wise addition of two matrices of equal shape."""

    # both are lists → recurse
    if isinstance(mat1, list) and isinstance(mat2, list):
        if len(mat1) != len(mat2):
            return None
        return [add_matrices(a, b) for a, b in zip(mat1, mat2)]

    # structure mismatch
    if isinstance(mat1, list) or isinstance(mat2, list):
        return None

    # base case (scalars)
    return mat1 + mat2
