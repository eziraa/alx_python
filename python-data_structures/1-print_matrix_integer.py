#!/bin/bash/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each element in the row and print it using str.format()
        for e in row:
            print("{:d}".format(e), end=' ' if e != row[len(row) - 1] else '')
        # Move to the next line after printing each row
        print()
