import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

num_col, num_row = map(int, input().split())

board = [list(map(int, input().split(" "))) for i in range(num_row)]
drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))

q = deque()
for i in range(num_row):
    for j in range(num_col):
        if board[i][j] == 1:
            q.append((i, j))

while q:
    row, col = q.popleft()
    for dr, dc in drdc:
        next_row = row + dr
        next_col = col + dc

        if 0 <= next_row < num_row and 0 <= next_col < num_col and board[next_row][next_col] == 0:
            board[next_row][next_col] = board[row][col] + 1
            q.append((next_row, next_col))

is_not_change = float('inf')
max_val = 0
for i in range(num_row):
    for j in range(num_col):
        if board[i][j] == 0:
            is_not_change = 0
        else:
            max_val = max(max_val, board[i][j])

print(min(max_val, is_not_change) - 1)