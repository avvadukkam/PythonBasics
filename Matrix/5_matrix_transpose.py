# Brute Force
def mat_transpose(A):
    temp_mat = [[0,0,0],[0,0,0]]
    for i in range(len(A[0])):
        for j in range(len(A)):
            temp_mat[i][j] = A[j][i]
    return temp_mat

A = [[1,2],[3,4],[5,6]]
print(mat_transpose(A))

#