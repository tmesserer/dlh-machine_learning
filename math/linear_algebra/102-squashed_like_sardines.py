#!/usr/bin/env python3
"""Module for linear algebra"""


def cat_matrices(mat1, mat2, axis=0):
    """Matrix concatenation alongside a specified axis"""
    new_matrix = []
    #first part: drill down to right level
for i in range(0, axis):
    try:
        mat1[0]
        mat1 = mat1[0]
    except:
        return None

    #when at right dimension (still list, no number) --> concatenate:
    if isinstance(mat1, list) and isinstance(mat2, list):
        for i in range(len(mat1)):
            new_matrix.append(mat1 + mat2)
    else:
        return None




import numpy as np
import time
cat_matrices = __import__('102-squashed_like_sardines').cat_matrices

mat1 = [1, 2, 3]
mat2 = [4, 5, 6]
np_mat1 = np.array(mat1)
np_mat2 = np.array(mat2)

t0 = time.time()
m = cat_matrices(mat1, mat2)
t1 = time.time()
print(t1 - t0)
print(m)
t0 = time.time()
np.concatenate((np_mat1, np_mat2))
t1 = time.time()
print(t1 - t0, "\n")

print(mat1 + mat2)