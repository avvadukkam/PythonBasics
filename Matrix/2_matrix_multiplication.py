# Using nested for loop (Brute Force)
def matrix_mult(X, Y):
    multi_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                multi_matrix[i][j] += X[i][k]*Y[k][j]
    return multi_matrix

X = [[1,7,3],[3,5,6],[6,8,9]]
Y = [[1,1,1,2],[6,7,3,0],[4,5,9,1]]
print(matrix_mult(X,Y))

# Using nested list (zip())
A = [[1,7,3],[3,5,6],[6,8,9]]
B = [[1,1,1,2],[6,7,3,0],[4,5,9,1]]
result = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
print(result)

# Matrix Multiplication (Vectorized implementation)
import numpy as np
C = [[1,7,3],[3,5,6],[6,8,9]]
D = [[1,1,1,2],[6,7,3,0],[4,5,9,1]]
result1 = np.dot(C,D)
print(result1)