#!/usr/bin/env python3
"""module for bayesian probability calculations"""
import numpy as np


def likelihood(x, n, P):
    """
    function that calculates the likelihood of obtaining this data given
    hypothetical     probabilities of developing severe side effects
    Args:
        x: number of patients that develop severe side effects (binomial dist)
        n: total number of patients observed
        P: 1D numpy.ndarray containing the various hypothetical probabilities
           of developing severe side effects
    """
    if not isinstance(n, int) and n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) and n < 0:
        raise ValueError("x must be an integer that is greater than \
                          or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) and len(P) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if any(x < 0 or x > 1 for x in P):
        raise ValueError("All values in P must be in the range [0, 1]")

    # calculation of PMF for binomial dist
    result = []
    for p in P:
        pmf_formula = (
                (factorial(n) / (factorial(x) * factorial(n-x)))
                * (p**x) * ((1-p)**(n-x))
                )
        result.append(pmf_formula)
    return result


def factorial(n):
    """function for calculating the of an int == n factorial"""
    if n == 1:
        return 1
    return n * factorial(n-1)


factorial(6-3)
# pmf of binomial dist: (n over k) * p**k * (1-p)**(n-k)
# n trials
# p probability of success
# k number of success
"""
If any value in P is not in the range [0, 1], raise a ValueError
    with the message All values in P must be in the range [0, 1]
    ## --> double check
Returns: a 1D numpy.ndarray containing the likelihood of obtaining the data,
    x and n, for each probability in P, respectively
"""
