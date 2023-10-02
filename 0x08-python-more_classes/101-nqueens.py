#!/usr/bin/python3
import sys


def initial_board(n):
    board = []
    for i in range(n):
        board.append([])
    for i in range(n):
        for row in board:
            row.append(0)
    return board


def copy_board(board):
    if isinstance(board, list):
        return list(map(copy_board, board))
    return board


def get_sol(board):
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
                break
    return solution


def exclude(board, i, j):
    for x in range(i + 1, len(board)):
        board[x][j] = -1
    for x in range(i - 1, -1, -1):
        board[x][j] = -1
    for x in range(j + 1, len(board)):
        board[i][x] = -1
    for x in range(j - 1, -1, -1):
        board[i][x] = -1

    column = j + 1
    for k in range(i + 1, len(board)):
        if column >= len(board):
            break
        board[k][column] = -1
        column += 1

    column = j - 1
    for k in range(i - 1, -1, -1):
        if column < 0:
            break
        board[k][column] = -1
        column -= 1

    column = j + 1
    for k in range(i - 1, -1, -1):
        if column >= len(board):
            break
        board[k][column] = -1
        column += 1

    column = j - 1
    for k in range(i + 1, len(board)):
        if column < 0:
            break
        board[k][column] = -1
        column -= 1


def solve(board, row, placed_queens, solutions):
    if placed_queens == len(board):
        solutions.append(get_sol(board))
        return solutions
    for i in range(len(board)):
        if board[row][i] == 0:
            temp = copy_board(board)
            temp[row][i] = 1
            exclude(temp, row, i)
            solutions = solve(temp, row + 1, placed_queens + 1, solutions)
    return solutions


if __name__ = "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if type(sys.argv[1]) is not int:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = initial_board(int(sys.argv[1]))
    solutions = solve(board, 0, 0, [])
    for solution in solutions:
        print(solution)
