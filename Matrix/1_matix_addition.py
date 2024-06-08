# Using for loop
def matrix_add(X, Y):
    added_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(X)):
        for j in range(len(X[0])):
            added_matrix[i][j] = X[i][j] + Y[i][j]
    return added_matrix


X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(matrix_add(X, Y))

# Using list comprehension
X1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
Y1 = [[90, 80, 70], [60, 50, 40], [30, 20, 10]]
result = [[X1[i][j]+Y1[i][j] for j in range(len(X1[0]))] for i in range(len(X1))]
print(result)

# Using zip()
X2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Y2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result2 = [*map(list,[map(sum, zip(*t)) for t in zip(X2, Y2)])]
print(result2)