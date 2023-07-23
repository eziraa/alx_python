#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for e in row:
            if e != row[-1]:
                print("{:d}".format(e), end=' ')
            else:
                print("{:d}".format(e), end='')
        print()
