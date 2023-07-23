#!/bin/bash/python3
def print_matrix_integer(matrix=[[]]):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    # Calculate the maximum width of each column to align the output
    column_widths = [max(len(str(matrix[row][col]))
                         for row in range(num_rows)) for col in range(num_cols)]

    # Print the matrix with proper formatting
    for row in matrix:
        for col_idx, value in enumerate(row):
            # Use str.format() to print each value with appropriate width
            print("{:>{width}}".format(
                value, width=column_widths[col_idx]), end=" ")
        print()  # Move to the next row after printing all values


# Test the function
matrix = [
    [1, 22, 333],
    [4444, 55555, 666666],
    [7777777, 88888888, 999999999]
]

print_matrix_integer(matrix)
