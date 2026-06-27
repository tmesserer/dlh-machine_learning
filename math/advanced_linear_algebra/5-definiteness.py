#!/usr/bin/env python3
"""Module for advanced linear algebra"""


def definiteness(matrix):
    """Determines the definiteness of a matrix"""
    import numpy as np
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not all(isinstance(row, list) for row in matrix):
        return None
    if not (all(len(row) == len(matrix) for row in matrix)) or not \
           (all(i is not None for row in matrix for i in row)):
        return None
    #if determinant(matrix) == 0:
        #return None
    """
    if isinstance(mat1, np.ndarray) is False:
        raise TypeError('matrix must be a numpy.ndarray')

    # calculate eigenvalues and definiteness
    try:
        ev, eigenvectors = np.linalg.eig(matrix)
    except Exception:
        return None
    if all(ev > 0):
        return "Positive definite"
    elif all(ev >= 0):
        return "Positive semi-definite"
    elif all(ev < 0):
        return "Negative definite"
    elif all(ev <= 0):
        return "Negative semi-definite"
    else:
        return "Indefinite"
