#!/usr/bin/env python3
"""Module for k-means clustering"""
import numpy as np


def variance(X, C):
    """function that calculates the total intra-cluster variance
    for a data set:
    Args:
        X is a numpy.ndarray of shape (n, d) containing the data set
        C is a numpy.ndarray of shape (k, d) containing the centroid means
          for each cluster

    Returns:
        var, or None on failure
        var is the total variance
    """
    try:
        X_reshaped = X[:, np.newaxis, :]
        X_squares = np.square(X_reshaped - C)
        sum_array = np.sum(X_squares, axis=2)
        result_sqrt = np.sqrt(sum_array)
        clss = np.argmin(result_sqrt, axis=1)
        n = X.shape[0]
        distance_point_cluster = sum_array[np.arange(n), clss]
        cluster_variance = np.sum(distance_point_cluster, axis=0)
        return cluster_variance

    except (ValueError, TypeError, AttributeError, IndexError):
        return None
