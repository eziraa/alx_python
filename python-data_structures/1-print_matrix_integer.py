#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each element in the row and print it using str.format()
        for e in row:
            if e != row[-1]:
                print("{:d}".format(e), end=' ')
            else:
                print("{:d}".format(e), end='')
        # Move to the next line after printing each row
        print()
