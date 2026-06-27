#!/usr/bin/env python3
"""Module for advanced linear algebra"""
import numpy as np


def definiteness(matrix):
    """Determines the definiteness of a matrix"""
    if isinstance(matrix, np.ndarray) is False:
        raise TypeError('matrix must be a numpy.ndarray')
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None
    if not np.array_equal(matrix, matrix.T):
        return None
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
