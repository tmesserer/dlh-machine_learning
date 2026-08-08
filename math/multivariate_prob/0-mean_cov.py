#!/usr/bin/env python3
"""module for multivariate probability"""
import numpy as np


def mean_cov(X):
    """function that calculates the mean and covariance
    of a dataset.
    Args: X: a numpy.ndarray of shape (n, d) containing
    the data set
    n = number of data points
    d = number of dimensions in each data point
    """
    if not isinstance(X, np.ndarray) or np.ndim(X) != 2:
        raise TypeError("X must be a 2d numpy.ndarray")
    if not isinstance(X, np.ndarray) or X.shape[0] < 2:
        raise ValueError("X must contain multiple data points")
    # Calculations
    # Mean
    sum_n = 0
    count_n = 0
    for row in X:
        sum_n += row
        count_n += 1
    mean = sum_n / count_n
    mean = np.reshape(mean, (1, len(X[0])))

    # Covariance
    n, d = X.shape
    init_matrix = np.zeros((d, d))
    for row in X:
        deviation = np.reshape(row, (1, len(X[0]))) - mean
        dev_row = np.reshape(deviation, (1, len(X[0])))
        dev_col = np.reshape(deviation, (len(X[0]), 1))
        outer_prod = np.matmul(dev_col, dev_row)
        init_matrix += outer_prod / (n-1)

    return mean, init_matrix
