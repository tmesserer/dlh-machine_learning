#!/usr/bin/env python3
"""Module for describing the poisson distribution"""
"""
π = 3.1415926536
e = 2.7182818285
er f(x) = ....
"""


class Poisson:
    """
    defines the class Poisson for Poisson probabilities
    """
    def __init__(self, data=None, lambtha=1.):
        """initiatilizes an instance under Poisson
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
            self.lambtha = (sum(data)/len(data))

    def pmf(self, k):
        """calculates the value of PMF for a number of successes
        Args:
        - self,
        - k
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        fact_k = 1
        for x in range(1, k):
            fact_k = fact_k * (x+1)
        return (((self.lambtha ** k) *
                 (2.7182818285 ** ((-1)*self.lambtha))) / fact_k)
