#!/usr/bin/env python3
"""Module for advanced linear algebra"""


def matrix_multiplication(mult_factor, matrix):
    """multiplies matrix by a constant factor"""
    new_matrix = []
    for i in range(0, len(matrix)):
        if not isinstance(matrix[i], list):
            new_matrix.append(matrix[i] * mult_factor)
        else:
            result = matrix_multiplication(mult_factor, matrix[i])
            new_matrix.append(result)
    return new_matrix


def add_matrices(mat1, mat2):
    """checks if matrices are same length.
    If they are, returns an element-wise addition."""
    if len(mat1) != len(mat2):
        return None
    sum_arr = []
    if not isinstance(mat1[0], list):
        for i in range(0, len(mat1)):
            sum_arr.append(mat1[i] + mat2[i])
    else:
        for i in range(0, len(mat1)):
            result = add_matrices(mat1[i], mat2[i])
            sum_arr.append(result)
    return sum_arr


def submatrix_calc(matrix, c):
    """calculates the minor matrix at element c
    Note: c refers to python length, not element of determinant
    """
    new_matrix = []
    new_row = []
    for i in range(1, len(matrix)):
        new_row.extend(matrix[i][:c])
        new_row.extend(matrix[i][c+1:])
        new_matrix.append(new_row)
        new_row = []
    return new_matrix


def determinant(matrix):
    """calculates the determinant of a matrix (list of lists)"""
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1

    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if len(matrix[0]) == 1:
        return matrix[0][0]
    elif len(matrix[0]) == 2:
        return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    else:
        result = 0
        for i in range(len(matrix[0])):
            minor = submatrix_calc(matrix, i)
            sign = (-1) ** i
            result += sign * matrix[0][i] * determinant(minor)
        return result


def minor_helper(matrix, m, n):
    """calculates the minor matrix without row m and column n
    Note: m, n refer to python length, not element of determinant
    """
    new_matrix = []
    new_row = []
    for i in range(0, len(matrix)):
        if m != i:
            new_row.extend(matrix[i][:n])
            new_row.extend(matrix[i][n+1:])
            new_matrix.append(new_row)
            new_row = []
    return new_matrix


def cofactor(matrix):
    """calculates the cofactor matrix of a matrix"""
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not (all(len(row) == len(matrix) for row in matrix)) or not \
           (all(i is not None for row in matrix for i in row)):
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return [[1]]
    new_row = []
    new_matrix = []
    for i in range(0, len(matrix)):  # each row
        for j in range(0, len(matrix[i])):  # each column
            det = determinant(minor_helper(matrix, i, j)) * (-1) ** (i + j)
            new_row.append(det)
        new_matrix.append(new_row)
        new_row = []
    return new_matrix


def adjugate(matrix):
    """creates the adjugate matrix of a matrix"""
    cofact = cofactor(matrix)
    new_row = []
    new_matrix = []
    for i in range(0, len(cofact)):  # each row
        for j in range(0, len(cofact[i])):  # each column
            new_row.append(cofact[j][i])
        new_matrix.append(new_row)
        new_row = []
    return new_matrix
