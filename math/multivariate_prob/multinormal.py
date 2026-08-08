#!/usr/bin/env python3
"""module for multivariate probability"""
import numpy as np


class MultiNormal:
    """
    data is a numpy.ndarray of shape (d, n) containing the data set:
    n is the number of data points
    d is the number of dimensions in each data point
    """
    def __init__(self, data):
        """initiation function"""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = np.shape(data)
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.data = data

        # Mean
        sum_n = 0
        data = data.T
        for row in data:
            sum_n += row
        mean = sum_n / n

        self.mean = np.reshape(mean, (d, 1))

        # Covariance
        init_matrix = np.zeros((d, d))
        for row in data:
            deviation = np.reshape(row, (1, d)) - mean
            dev_row = np.reshape(deviation, (1, d))
            dev_col = np.reshape(deviation, (d, 1))
            outer_prod = np.matmul(dev_col, dev_row)
            init_matrix += outer_prod / (n-1)

        self.cov = init_matrix

    def pdf(self, x):
        """calculates the PDF at a data point"""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.mean.shape[0]
        if np.shape(x) != (d, 1):
            raise ValueError(f"x must have the shape ({d}, 1)")
        denom = (2 * np.pi) ** (d/2) * (np.linalg.det(self.cov) ** (1/2))
        exp = np.exp((-1/2) * (((x - self.mean).T) @ np.linalg.inv(self.cov))
                     @ (x - self.mean))
        return (1 / denom) * exp
