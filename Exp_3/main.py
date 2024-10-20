from matrix_operations import read_matrix, multiply_matrices, write_matrix

# Read matrices from the CSV files
matrix1 = read_matrix('mat1.csv')
matrix2 = read_matrix('mat2.csv')
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)

# Multiply the matrices
result_matrix = multiply_matrices(matrix1, matrix2)

# Write the result to a new CSV file
write_matrix(result_matrix, 'result_matrix.csv')  # Save the output in result_matrix in the folder
print("Resulting Matrix saved in 'result_matrix.csv'")

# Read and print the resulting matrix from the CSV file
result_matrix = read_matrix('result_matrix.csv')
print("Resulting Matrix:")
print(result_matrix)
