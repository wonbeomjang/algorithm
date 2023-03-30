import sys
from collections import deque
from copy import deepcopy

input = lambda: sys.stdin.readline().strip()
drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))
answer = 0


num_row, num_col = map(int, input().split())
board = [list(map(int, input().split())) for i in range(num_row)]


def print_board(board):
    for line in board:
        print(" ".join(map(str, line)))


def bfs(q, board):
    while q:
        row, col = q.popleft()

        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc

            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                continue

            if board[next_row][next_col] == 0:
                board[next_row][next_col] = 2
                q.append((next_row, next_col))


def count_zero(board):
    zeros = 0
    for i in range(num_row):
        for j in range(num_col):
            if board[i][j] == 0:
                zeros += 1
    return zeros

q = deque()

for i in range(num_row):
    for j in range(num_col):
        if board[i][j] == 2:
            q.append((i, j))


def dfs(board, n):
    global answer

    if n == 3:
        bfs(deepcopy(q), board)
        answer = max(answer, count_zero(board))
        return

    for i in range(num_row):
        for j in range(num_col):
            if board[i][j] == 0:
                temp = deepcopy(board)
                temp[i][j] = 1
                dfs(temp, n + 1)


dfs(board, 0)

print(answer)