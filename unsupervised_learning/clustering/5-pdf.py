#!/usr/bin/env python3
"""Module for k-means clustering"""
import numpy as np


def pdf(X, m, S):
    """function that calculates the probability density function of a
    Gaussian distribution:
    Args:
        X is a numpy.ndarray of shape (n, d) containing the data points
            whose PDF should be evaluated
        m is a numpy.ndarray of shape (d,) containing the mean of the
            distribution
        S is a numpy.ndarray of shape (d, d) containing the covariance
             of the distribution

    Returns: pi, m, S, or None, None, None on failure

    pi is a numpy.ndarray of shape (k,) containing the priors for each
        cluster, initialized evenly
    m is a numpy.ndarray of shape (k, d) containing the centroid means
        for each cluster, initialized with K-means
    S is a numpy.ndarray of shape (k, d, d) containing the covariance
        matrices for each cluster, initialized as identity matrices
    """
    try:
        scalar = 1 / (np.sqrt((2 * np.pi) ** S.shape[0]) * np.linalg.det(S))
        diff = X - m
        pdf = np.e ** np.sum((-(1/2) * diff @ np.linalg.inv(S) * diff), axis=1)
        P = np.maximum(scalar * pdf, 1e-300)
        return P

    except (ValueError, TypeError, AttributeError, IndexError):
        return None
