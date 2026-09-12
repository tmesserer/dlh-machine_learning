#!/usr/bin/env python3
"""Module for k-means clustering"""
import numpy as np


def kmeans(X, k, iterations=1000):
    """function that performs K-means on a dataset
    Args:
        X is a numpy.ndarray of shape (n, d) containing the dataset that
        will be used for K-means
         clustering:
            n is the number of data points
            d is the number of dimensions for each data point
        k is a positive integer containing the number of clusters

    Returns: a numpy.ndarray of shape (k, d) containing the initialized
    centroids for each cluster,
    or None on failure
    """
    try:
        if not isinstance(k, int) or k <= 0:
            raise ValueError
        if not isinstance(iterations, int) or iterations <= 0:
            raise ValueError
        min_X = np.min(X, axis=0)
        max_X = np.max(X, axis=0)
        d = X.shape[1]
        size = [k, X.shape[1]]
        C = np.random.uniform(min_X, max_X, size)
        counter = 0
        while counter < iterations:
            X_reshaped = X[:, np.newaxis, :]
            X_squares = np.square(X_reshaped - C)
            sum_array = np.sum(X_squares, axis=2)
            result_sqrt = np.sqrt(sum_array)

            clss = np.argmin(result_sqrt, axis=1)
            C_old = np.copy(C)

            for i in range(0, k):
                points_in_cluster = X[clss == i]
                if len(points_in_cluster) == 0:
                    C[i] = np.random.uniform(min_X, max_X, d)
                else:
                    C[i] = np.mean(points_in_cluster, axis=0)
            if np.array_equal(C_old, C):
                return C, clss
            counter += 1

        # recompute clss one final time against the last-updated C
        X_reshaped = X[:, np.newaxis, :]
        sum_array = np.sum(np.square(X_reshaped - C), axis=2)
        clss = np.argmin(sum_array, axis=1)
        return C, clss

    except(ValueError, TypeError, AttributeError, IndexError):
        return None, None
