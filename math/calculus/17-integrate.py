#!/usr/bin/env python3
"""Module for calculus project"""


def poly_integral(poly, C=0):
    """calculates the integral of a polynomial"""
    if not isinstance(poly, list) or not all(isinstance(x, int) for x in poly)\
       or poly == []:
        return None
    new_poly = []
    if isinstance(C, int):
        new_poly.append(C)
        new_poly.extend([int(poly[i] / (i+1)) if poly[i] % (i+1) == 0
                         else poly[i] / (i+1) for i in range(0, len(poly))])
        while len(new_poly) > 1 and new_poly[-1] == 0:
            new_poly.pop()
        return new_poly
    else:
        return None
