#!/usr/bin/env python3
"""Module for calculus project"""


def summation_i_squared(n):
    """sums all numbers squared until n"""
    if n < 1:
        return None
    return int(n * ((n+1) * ((2*n)+1))/6)
