# list comprehension to find the transpose of a matrix
matrix_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
transpose_list = [[matrix_list[i][j] for j in range(len(matrix_list))] for i in range(len(matrix_list[0]))]
print(transpose_list)
