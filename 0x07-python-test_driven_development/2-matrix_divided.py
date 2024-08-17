#!/usr/bin/python3
def matrix_divided(matrix, div):
    """devide the matrix elements by div (interger)

    Args:
        matrix (list(list)): the first argument and the martrix to be devided
        div (int, float): the second argument and the number to devide by
    Return:
        list(list): new matirx that contain the result of deviding
                    matrix element by the div
    Raise:
        TypeError: if the matrix is not list of list
                   if size of each row is not compatible
                   if div is not a number
        ZeroDevisionError: if div equal to zero
    """
    if (not isinstance(matrix, list) or matrix == []
            or not all(isinstance(row, list)
            and all(isinstance(c, (int, float))
            for c in row) for row in matrix)):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                    )
        for c in row:
            if not isinstance(c, (int, float)):
                raise TypeError(
                            "matrix must be a matrix (list of lists) of integers/floats"
                                )
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    new = []
    for r in matrix:
        new_row = []
        for c in r:
            new_row.append(round(c / div, 2))
        new.append(new_row)
    return new
