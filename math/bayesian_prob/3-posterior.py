#!/usr/bin/env python3
"""module for bayesian probability calculations"""
import numpy as np


# Posterior = Likelihood * Prior / Marginal Probability
# Likelihood * prior = intersection
# P(A | B) = P(B | A) * P(A) / P(B)
def posterior(x, n, P, Pr):
    """
    function that calculates the posterior probability for the various
    hypothetical probabilities of developing severe side effects
    given the data.
    Args:
        x: number of patients that develop severe side effects (binomial dist)
        n: total number of patients observed
        P: 1D numpy.ndarray containing the various hypothetical probabilities
           of developing severe side effects
        Pr: 1d numpy.ndarray, prior beliefs of P
    """
    # Exceptions:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or np.ndim(P) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or np.shape(P) != np.shape(Pr):
        raise TypeError(
            "Pr must be a numpy.ndarray with the same shape as P")
    if any(x < 0 or x > 1 for x in P):
        raise ValueError("All values in P must be in the range [0, 1]")
    if any(y < 0 or y > 1 for y in Pr):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(1, np.sum(Pr), rtol=0.00001, atol=0.00001):
        raise ValueError("Pr must sum to 1")

    # Calculation
    result = []
    for p in P:
        pmf_formula = (
                (factorial(n) / (factorial(x) * factorial(n-x)))
                * (p**x) * ((1-p)**(n-x))
                )
        result.append(pmf_formula)
    likelihood = result
    marg_prob = np.sum(np.multiply(np.array(result), Pr))
    intersection = np.multiply(np.array(result), Pr)
    # print("likelihood: {}, marginal probability: {}, \
    # prior: {}".format(likelihood, marg_prob, prior))
    return intersection / marg_prob


def factorial(n):
    """function for calculating the of an int == n factorial"""
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)
