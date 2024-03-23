#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_element = len(row)
        col = 0

        for i in row:
            if col < row_elements - 1:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
            col += 1
        print()
