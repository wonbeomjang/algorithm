import copy
import sys

board = [list(map(int, list(input()))) for i in range(9)]
zero_pos = [(i, j) for i in range(9) for j in range(9) if not board[i][j]]
_candidate = list(range(1, 10))


def dfs(cnt):
    if cnt == len(zero_pos):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end="")
            print()
        sys.exit(0)

    row, col = zero_pos[cnt]
    candidate = copy.deepcopy(_candidate)

    start_row = row // 3 * 3
    start_col = col // 3 * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] in candidate:
                candidate.remove(board[i][j])

    for i in range(9):
        if board[i][col] in candidate:
            candidate.remove(board[i][col])

    for j in range(9):
        if board[row][j] in candidate:
            candidate.remove(board[row][j])

    for can in candidate:
        board[row][col] = can
        dfs(cnt + 1)
    board[row][col] = 0

dfs(0)
