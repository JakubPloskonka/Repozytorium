def multiply_matrices(matrix_a, matrix_b):


    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])


    if cols_a != rows_b:
        raise ValueError("Number of columns in matrix A must be equal to the number of rows in matrix B")


    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]


    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

# Example
if __name__ == "__main__":
    # Define two matrices
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    matrix_b = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    # Multiply the matrices
    try:
        result = multiply_matrices(matrix_a, matrix_b)
        print("Resultant Matrix:")
        for row in result:
            print(row)
    except ValueError as e:
        print(e)
