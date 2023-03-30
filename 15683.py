import sys
from copy import deepcopy


input = lambda: sys.stdin.readline().strip()
drdc = ((-1, 0), (0, -1), (1, 0), (0, 1))
num_rows, num_cols = map(int, input().split())
answer = float('inf')


def look(row, col, board, direction):
    while True:
        row, col = row + drdc[direction][0], col + drdc[direction][1]
        if not (0 <= row < num_rows and 0 <= col < num_cols):
            break
        if board[row][col] == 6:
            break
        if board[row][col] == 0:
            board[row][col] = 9


def count_zero(board):
    num_zeros = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if board[i][j] == 0:
                num_zeros += 1

    return num_zeros


def cctv(row, col, cctv_type, board, direction):
    if cctv_type == 1:
        look(row, col, board, direction)
    elif cctv_type == 2:
        look(row, col, board, direction)
        look(row, col, board, (direction + 2) % 4)
    elif cctv_type == 3:
        look(row, col, board, direction)
        look(row, col, board, (direction + 1) % 4)
    elif cctv_type == 4:
        look(row, col, board, direction)
        look(row, col, board, (direction + 1) % 4)
        look(row, col, board, (direction + 2) % 4)


def dfs(board, n):
    global answer

    if n == len(cctv_info):
        answer = min(answer, count_zero(board))
        return

    for direction in range(4):
        copyed_board = deepcopy(board)
        row, col, cctv_type = cctv_info[n]
        cctv(row, col, cctv_type, copyed_board, direction)
        dfs(copyed_board, n + 1)


def print_board(board):
    for line in board:
        print(" ".join(map(str, line)))


cctv_info = []
board = [list(map(int, input().split())) for i in range(num_rows)]

for i in range(num_rows):
    for j in range(num_cols):
        if 0 < board[i][j] < 5:
            cctv_info += [(i, j, board[i][j])]
        if board[i][j] == 5:
            look(i, j, board, 0)
            look(i, j, board, 1)
            look(i, j, board, 2)
            look(i, j, board, 3)

dfs(board, 0)
print(answer)