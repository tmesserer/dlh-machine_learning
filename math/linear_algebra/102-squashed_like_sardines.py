#!/usr/bin/env python3
"""Module for linear algebra"""


def cat_matrices(mat1, mat2, axis=0):
    """Matrix concatenation alongside a specified axis"""
    new_matrix = []
    #first part: drill down to right level with zip once for each axis
    if axis > 0 and len(mat1) == len(mat2):
        return [cat_matrices(m1, m2, axis - 1) for m1, m2 in zip(mat1, mat2)]
    #elif len(mat1) != len(mat2):
        #return "lenghts of matrices unequal"
    
    #when at right dimension (still list, no number) --> concatenate:
    # if isinstance(mat1, list) and isinstance(mat2, list):
    new_matrix.append(mat1 + mat2)
    return new_matrix
    #else:
        #return None

"""
mat1 = [1, 2, 3]
mat2 = [4, 5, 6]
cat_matrices(mat1, mat2, axis = 0)

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
cat_matrices(mat1, mat2, axis = 0)
cat_matrices(mat1, mat2, axis = 1)

mat3 = [[[[1, 2, 3, 4], [5, 6, 7, 8]],
         [[9, 10, 11, 12], [13, 14 ,15, 16]],
         [[17, 18, 19, 20], [21, 22, 23, 24]]],
        [[[25, 26, 27, 28], [29, 30, 31, 32]],
         [[33, 34, 35, 36], [37, 38, 39, 40]],
         [[41, 42, 43, 44], [45, 46, 47, 48]]]]
mat4 = [[[[11, 12, 13, 14], [15, 16, 17, 18]],
         [[19, 110, 111, 112], [113, 114 ,115, 116]],
         [[117, 118, 119, 120], [121, 122, 123, 124]]],
        [[[125, 126, 127, 128], [129, 130, 131, 132]],
         [[133, 134, 135, 136], [137, 138, 139, 140]],
         [[141, 142, 143, 144], [145, 146, 147, 148]]]]
mat5 = [[[[11, 12, 13, 14], [15, 16, 17, 18]],
         [[117, 118, 119, 120], [121, 122, 123, 124]]],
        [[[125, 126, 127, 128], [129, 130, 131, 132]],
         [[141, 142, 143, 144], [145, 146, 147, 148]]]]
cat_matrices(mat3, mat4, axis=3)
cat_matrices(mat3, mat5, axis=1)

"""
