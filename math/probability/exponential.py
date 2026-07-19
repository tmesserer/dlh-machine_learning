#!/usr/bin/env python3
"""Module for describing the poisson distribution"""
"""
e = 2.7182818285
"""


class Exponential:
    """
    defines the class Exponential for exp. probabilities
    """
    def __init__(self, data=None, lambtha=1.):
        """initiatilizes an instance under Exponential
        Args:
            data: validity checks, list of data
            lambtha: validity check, calculates it based on data if not given
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.data = data
            self.lambtha = 1/(sum(data)/len(data))

    def pdf(self, x):
        """calculates the value of PMF for a number of successes
        Args:
        - self,
        - x
        """
        if x < 0:
            return 0
        return (self.lambtha * (2.7182818285 ** (-self.lambtha * x)))

    def cdf(self, x):
        """calculates the value of CDF for exponential dist
        Args:
        - self,
        - x
        """
        if x < 0:
            return 0
        return (1 - (2.7182818285 ** (- self.lambtha * x)))
