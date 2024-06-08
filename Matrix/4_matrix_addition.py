# Brute Force
def mat_addition(mat1, mat2):
    sum_mat = [[0, 0], [0, 0]]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            sum_mat[i][j] = mat1[i][j] + mat2[i][j]
    return sum_mat


def mat_substraction(mat1, mat2):
    sub_mat = [[0, 0], [0, 0]]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            sub_mat[i][j] = mat1[i][j] - mat2[i][j]
    return sub_mat


mat1 = [[1, 2], [3, 4]]
mat2 = [[4, 5], [6, 7]]
print("A+B = ", mat_addition(mat1, mat2))
print("A-B = ", mat_substraction(mat1, mat2))

# Using np.add()
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 5], [6, 7]])
print("A+B = \n", np.add(A, B))
print("A-B = \n", np.subtract(A, B))
