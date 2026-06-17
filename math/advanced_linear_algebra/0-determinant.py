#!/usr/bin/env python3
"""Module for advanced linear algebra"""
    

def determinant(matrix):
    """calculates the determinant of a matrix (list of lists)"""
    try:
        if matrix == [[]]:
            print("empty Matrix")
            return 1
            
        elif len(matrix[0]) == 1 and isinstance(matrix[0][0], int):
            print("1x1 Matrix")
            return matrix[0]

        elif len(matrix[0]) == 2 and isinstance(matrix[0][0], int) and isinstance(matrix[0][1], int):
            print("2x2 Matrix")
            return [(matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])]

        #3x3 and beyond    
        else:
            print("pass")
            return len(matrix[0]) * #add rest
        #determinant(cofactor matrix1)
        
    #Exceptions    
    except TypeError: #not a list of lists
        return "matrix must be a list of lists"
    except ValueError: #not a square matrix
        return "matrix must be a square matrix"

mat0 = [[]]
mat1 = [[5]]
mat2 = [[1, 2], [3, 4]]
mat3 = [[1, 1], [1, 1]]
mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
mat5 = []
mat6 = [[1, 2, 3], [4, 5, 6]]

len(mat1)
len(mat1[0])
print(isinstance(mat1[0][0], int))

determinant(mat0)
determinant(mat1)
determinant(mat2)
determinant(mat3)


mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
for i in range(0, len(mat4[0])):
    print(i)
    mat4[0][i] * ()
    for j in range(0, len(mat4[0])):
        if j == i:
            pass
        #add the cofactor matrix


print(mat4[0])