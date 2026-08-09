#!/usr/bin/env python3
"""module for bayesian probability calculations"""
from scipy import special


# Posterior = Likelihood * Prior / Marginal Probability
# Likelihood * prior = intersection
# P(A | B) = P(B | A) * P(A) / P(B)
def posterior(x, n, p1, p2):
    """
    function that calculates the posterior probability for the various
    hypothetical probabilities of developing severe side effects
    given the data.
    Args:
        x: number of patients that develop severe side effects (binomial dist)
        n: total number of patients observed
        p1 is the lower bound on the range
        p2 is the upper bound on the range
    """
    # Exceptions:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(p1, float) or (p1 < 0 or p1 > 1):
        raise ValueError("p1 must be a float in the range [0, 1]")
    if not isinstance(p2, float) or (p2 < 0 or p2 > 1):
        raise ValueError("p2 must be a float in the range [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")
    # Calculation
    a = x + 1
    b = n - x + 1
    return special.betainc(a, b, p2) - special.betainc(a, b, p1)
