#!/usr/bin/env python3
"""module for multivariate probability"""
import numpy as np


def correlation(C):
    """function that calculates a correlation matrix.
    Args: C: a numpy.ndarray of shape (d, d) containing
    a covariance matrix"""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")
    # Calculations
    variances = np.diag(C)  # gives a (d, ) array of the diagonal
    std = np.sqrt(variances)
    std_row = np.reshape(std, (1, len(std)))
    std_col = np.reshape(std, (len(std), 1))
    denom_matrix = std_col * std_row
    return C / denom_matrix
