#!/usr/bin/python3
import sys
"""
a program that solves the N queens problem
"""


def is_ok(b, row, col):
    """
    Function check if it's safe to place a queen

    Args:
        b: A list of the current state of the chessboard
        row: index of row
        col: column index.

    Return:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for k in range(row):
        if b[k][col] == 1:
            return False

    k, j = row, col
    while k >= 0 and j >= 0:
        if b[k][j] == 1:
            return False
        k -= 1
        j -= 1

    k, j = row, col
    while k >= 0 and j < len(b):
        if b[k][j] == 1:
            return False
        k -= 1
        j += 1
    return True


def solve_nqueens(num):
    """
    Function solve the N Queens problem and print all solutions.

    Args:
        num: The size of the chessboard.
    """
    b = [[0] * num for _ in range(num)]
    solt = []
    solve_u(b, 0, solt)
    print_s(solt)


def solve_u(board, row, solt):
    """
    function to solve the N Queens problem

    Args:
        board: state of the chessboard.
        row: The current row index.
        solt: List to store the solutions.
    """
    if row == len(board):
        solutions = []
        for f in range(len(board)):
            for j in range(len(board)):
                if board[f][j] == 1:
                    solutions.append([f, j])
        solt.append(solutions)
        return

    for c in range(len(board)):
        if is_ok(board, row, c):
            board[row][c] = 1
            solve_u(board, row + 1, solt)
            board[row][c] = 0


def print_s(solts):
    """
    Print all  solutions to the N Queens problem.

    Arg:
        solts: List of solutions.
    """
    for s in solts:
        print(s)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        so = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if so < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(so)
