#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[]]

    for row in matrix:
        list = []
        for cell in row:
            list.append(cell ** 2)
        new_matrix.append(list)
    new_matrix.remove([]) if [] not in matrix else new_matrix
    return new_matrix


print(square_matrix_simple([[4, 1, 4], [4, 52, 5]]))
