# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i + 1}: ").split()
        while len(row) != cols:
            print(f"Error: Please enter exactly {cols} numbers.")
            row = input(f"Enter row {i + 1}: ").split()
        matrix.append([int(x) for x in row])
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f"{num:>4}", end="")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(new_row)
    return result


def multiply_matrices(matrix1, matrix2):
    m = len(matrix1)
    n = len(matrix1[0])
    p = len(matrix2[0])
    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += matrix1[i][k] * matrix2[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


if __name__ == "__main__":
    print("=" * 50)
    print("PART A — Transpose a Matrix")
    print("=" * 50)
    
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    print("\nEnter the matrix:")
    matrix = read_matrix(rows, cols)
    
    print("\nOriginal Matrix:")
    print_matrix(matrix)
    
    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(transposed)
    
    print("\n" + "=" * 50)
    print("PART B — Add Two Matrices")
    print("=" * 50)
    
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    print("\nEnter first matrix:")
    matrix1 = read_matrix(rows, cols)
    
    print("\nEnter second matrix:")
    matrix2 = read_matrix(rows, cols)
    
    print("\nMatrix 1:")
    print_matrix(matrix1)
    print("\nMatrix 2:")
    print_matrix(matrix2)
    
    sum_matrix = add_matrices(matrix1, matrix2)
    print("\nSum Matrix:")
    print_matrix(sum_matrix)
    
    print("\n" + "=" * 50)
    print("PART C — Multiply Two Matrices")
    print("=" * 50)
    
    m = int(input("Enter rows for matrix A: "))
    n = int(input("Enter columns for matrix A: "))
    
    print("\nEnter matrix A:")
    matrixA = read_matrix(m, n)
    
    n2 = int(input("Enter rows for matrix B: "))
    p = int(input("Enter columns for matrix B: "))
    
    while n != n2:
        print(f"Error: Matrix A has {n} columns but Matrix B has {n2} rows.")
        print("Columns of A must equal rows of B.")
        n2 = int(input("Enter rows for matrix B: "))
    
    print("\nEnter matrix B:")
    matrixB = read_matrix(n2, p)
    
    print("\nMatrix A:")
    print_matrix(matrixA)
    print("\nMatrix B:")
    print_matrix(matrixB)
    
    product = multiply_matrices(matrixA, matrixB)
    print("\nProduct Matrix (A × B):")
    print_matrix(product)
