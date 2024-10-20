# matrix_operations.py

def generate_matrix(x, y, z):
    """Generate a 3D matrix with indices x, y, z."""
    matrix = [[[0 for _ in range(z)] for _ in range(y)] for _ in range(x)]

    for i in range(x):
        for j in range(y):
            for k in range(z):
                sum_indices = i + j + k
                if (sum_indices % 10 == 2) or (sum_indices % 10 == 6):
                    matrix[i][j][k] = 0  # Even sum of indices
                else:
                    matrix[i][j][k] = 1  # Odd sum of indices

    return matrix

def longest_substring(matrix):
    """Find the longest substring of 1s in a 3D matrix."""
    x, y, z = len(matrix), len(matrix[0]), len(matrix[0][0])
    max_length = 0
    max_position = None
    longest_coordinates = []  # List to store the coordinates of the longest substring

    for i in range(x):
        for j in range(y):
            current_length = 0
            current_coordinates = []  # Temporarily store coordinates for the current row

            for k in range(z):
                if matrix[i][j][k] == 1:
                    current_coordinates.append((i, j, k))  # Store the coordinate
                    current_length += 1

                    if current_length > max_length:
                        max_length = current_length
                        max_position = (i, j, k - current_length + 1)
                        longest_coordinates = current_coordinates.copy()  # Update the longest coordinates
                else:
                    current_length = 0
                    current_coordinates = []  # Reset the temporary coordinates if a 0 is encountered

    return max_length, max_position, longest_coordinates
