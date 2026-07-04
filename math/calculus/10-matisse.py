#!/usr/bin/env python3
"""Module for calculus project"""


def poly_derivative(poly):
    """calculates the derivative of a polynomial"""
    if not isinstance(poly, list) or not all(isinstance(x, int) for x in poly)\
       or poly == []:
        return None
    new_poly = [poly[i] * i for i in range(1, len(poly))]
    return new_poly if new_poly else [0]
