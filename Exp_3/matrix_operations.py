# matrix_operations.py

# Function to read a matrix from a CSV file
def read_matrix(filename):
    matrix = []
    with open(filename, "r", encoding='utf-8-sig') as file:  # Open filename for reading
        for line in file:
            row = list(map(int, line.strip().split(',')))  # Strip whitespaces & split the lines with comma
            matrix.append(row)  # Append processed row to matrix list
    return matrix

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Initialize 3x3 matrix
    for i in range(3):  # Iterate over the rows of matrix1
        for j in range(3):  # Iterate over the columns of matrix2
            for k in range(3):  # Iterate over the elements of the current row of matrix1 and the current column of matrix2
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# Function to write a matrix to a CSV file
def write_matrix(matrix, filename):
    with open(filename, "w") as file:  # Open filename for writing
        for row in matrix:
            file.write(','.join(map(str, row)) + '\n')  # Convert each element in the row to a string, join elements with comma
