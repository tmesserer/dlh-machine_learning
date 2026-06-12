#!/usr/bin/env python3
"""Module for linear algebra"""


def matrix_shape(matrix):
    """returns the shape of a matrix.
    args: matrix
    """
    shape = []
    this_row = matrix

    while isinstance(this_row, list):
        if not this_row:
            return [0]
        shape.append(len(this_row))
        this_row = this_row[0]
    return shape


def cat_matrices(mat1, mat2, axis=0):
    """Matrix concatenation alongside a specified axis"""
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)

    if axis >= len(shape1) or axis >= len(shape2):
        return None

    # remove the element at index `axis` from each shape,
    # then compare the rest
    if (shape1[:axis] + shape1[axis + 1:]
            != shape2[:axis] + shape2[axis + 1:]):
        return None

    if axis > 0:
        return [cat_matrices(m1, m2, axis - 1) for m1, m2 in zip(mat1, mat2)]

    return mat1 + mat2


"""
def matrix_shape(matrix):
    """
# returns the shape of a matrix.
# args: matrix
"""
    this_row = matrix
    shape = []

    while isinstance(this_row, list):
        if not this_row:
            return [0]
            break
        shape.append(len(this_row))
        this_row = this_row[0]
    return shape


def cat_matrices(mat1, mat2, axis=0):
    # Matrix concatenation alongside a specified axis
    """
"""
    if axis == 0 and (
        isinstance(mat1[0], list) != isinstance(mat2[0], list)
        or (isinstance(mat1[0], list) and len(mat1[0]) != len(mat2[0]))
    ):
        return None

    if axis > 0:
        if len(mat1) != len(mat2):
            return None
        return [cat_matrices(m1, m2, axis - 1) for m1, m2 in zip(mat1, mat2)]

    return mat1 + mat2




mat1 = [1, 2, 3]
mat2 = [4, 5, 6, 7]
new_matrix = mat1 + mat2
print(new_matrix)
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

matrix_shape(mat3)
matrix_shape(mat4)
matrix_shape(mat5)

matrix_shape(mat3)
my_shape = [2, 3, 2 ,4]
print(my_shape[0])
"""
