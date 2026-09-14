#!/usr/bin/env python3
"""Module for k-means clustering"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """function that tests for the optimum number of clusters by
    variance:
    Args:
        X is a numpy.ndarray of shape (n, d) containing the data set
        k is a positive integer containing the number of clusters

    Returns: pi, m, S, or None, None, None on failure

    pi is a numpy.ndarray of shape (k,) containing the priors for each
        cluster, initialized evenly
    m is a numpy.ndarray of shape (k, d) containing the centroid means
        for each cluster, initialized with K-means
    S is a numpy.ndarray of shape (k, d, d) containing the covariance
        matrices for each cluster, initialized as identity matrices
    """
    try:
        if not isinstance(k, int) or k <= 0:
            raise ValueError
        C, index = kmeans(X, k, iterations=1000)
        pi = np.array(np.tile(1/k, k))
        m = C
        ident_mat = np.identity(X.shape[1])
        S = np.tile(ident_mat, (k, 1, 1))
        return pi, m, S

    except (ValueError, TypeError, AttributeError, IndexError):
        return None, None, None
