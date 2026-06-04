#!/usr/bin/env python3
"""Module for linear algebra"""


def matrix_transpose(matrix):
    """resturns the shape of a matrix.
    args: matrix
    """
    new_matrix = []
    this_row = matrix
    #while isinstance(this_row[0], list):
        #this_row = this_row[0]
    #if not this_row:
        #return [0]
        #break
    new_matrix = []
    for i in range(0, len(this_row[0])):
        for j in range(0, len(this_row)):
            new_row = []
            new_row.append(this_row[j][i])
            print(new_row)
        new_matrix.append(new_row)
        print(new_matrix)

mat1 = [[1, 2], [3, 4]]
mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]

matrix_transpose(mat1)

"""
for i in this_row:
    print(f"i: {i}, value: {this_row[i]}")
    for j in range(0, len(this_row)):
        print(f"j: {j}, value: {this_row[i]}")
        new_matrix.append(this_row[j])
shape.append(len(this_row))
return new_matrix
"""

