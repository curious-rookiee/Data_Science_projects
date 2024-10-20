# main.py

from matrix_operations import generate_matrix, longest_substring

def main():
    x_dim, y_dim, z_dim = 7, 5, 3
    # Generate the 3D matrix
    matrix = generate_matrix(x_dim, y_dim, z_dim)

    # Output the matrix
    for i in range(x_dim):
        for j in range(y_dim):
            for k in range(z_dim):
                print(f"matrix[{i}][{j}][{k}] = {matrix[i][j][k]}")
            print()
        print()

    longest_length, start_position, coordinates = longest_substring(matrix)
    print(f"Longest substring of 1s length: {longest_length}")
    print(f"Starting position of longest substring: {start_position}")
    print("Coordinates of longest substring:")
    for coord in coordinates:
        print(coord)

if __name__ == "__main__":
    main()
