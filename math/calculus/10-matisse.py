#!/usr/bin/env python3
"""Module for calculus project"""


def poly_derivative(poly):
    """calculates the derivative of a polynomial"""
    if not isinstance(poly, list) or not all(isinstance(x, int) for x in poly)\
       or poly == []:
        return None
    new_poly = []
    for i in range(1, len(poly)):
        new_poly.append(poly[i] * i)
    return new_poly


"""
poly = [5, 0, 4, 2]
poly_derivative(poly)

poly = [5, 3, "a", 1]
print(poly[1])
#c, x, x^2, x^3
for i in range(1, len(poly)):
    print(poly[i])
    print(poly)
    print(poly[1])


poly = [5, 3, 4, 2]

#3, 8, 6
for i in range(1, len(poly)):
    print(poly[i] * i)

poly = [5, 3, 4, 2]
new_poly = []
#3, 8, 6
for i in range(1, len(poly)):
    new_poly.append(poly[i] * i)
print(new_poly)
"""
