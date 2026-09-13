#!/usr/bin/env python3
"""Module for k-means clustering"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """function that tests for the optimum number of clusters by 
    variance:
    Args:
        X is a numpy.ndarray of shape (n, d) containing the data set
        kmin is a positive integer containing the minimum number of clusters
        to check for (inclusive)
        kmax is a positive integer containing the maximum number of clusters
        to check for (inclusive)
        iterations is a positive integer containing the maximum number of iterations
        for K-means

    Returns:
        results, d_vars, or None, None on failure
    """
    try:
        if not isinstance(kmin, int) or kmin <= 0:
            raise ValueError
        if not isinstance(iterations, int) or iterations <= 0:
            raise ValueError
        if not kmax or kmax > X.shape[0]:
            kmax = X.shape[0]
        if not isinstance(kmax, int) or kmax <= 0:
            raise ValueError
        elif kmin > kmax:
            raise ValueError
        results = []
        d_vars = []
        if kmin == kmax:
            kmax = kmin + 1
        for k in range(kmin, kmax+1):
            C, clss = kmeans(X, k, iterations)
            results.append((C, clss))
            if k == kmin:
                smallest_variance = variance(X, C)
                d_vars.append(smallest_variance - smallest_variance) # 0
            else:
                d_vars.append(variance(X, C) - smallest_variance)
        return results, d_vars

    except (ValueError, TypeError, AttributeError, IndexError):
        return None, None

np.random.seed(0)
a = np.random.multivariate_normal([30, 40], [[16, 0], [0, 16]], size=50)
b = np.random.multivariate_normal([10, 25], [[16, 0], [0, 16]], size=50)
c = np.random.multivariate_normal([40, 20], [[16, 0], [0, 16]], size=50)
d = np.random.multivariate_normal([60, 30], [[16, 0], [0, 16]], size=50)
e = np.random.multivariate_normal([20, 70], [[16, 0], [0, 16]], size=50)
X = np.concatenate((a, b, c, d, e), axis=0)

kmeans(X, X.shape[0])