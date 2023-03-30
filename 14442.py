import sys
from collections import deque


drdc = ((1, 0), (0, 1), (-1, 0), (0, -1))
input = lambda: sys.stdin.readline().strip()

num_rows, num_cols, can_break = map(int, input().split())

board = [list(map(int, list(input()))) for i in range(num_rows)]

visited = [[[float('inf')] * (can_break + 1) for _ in range(num_cols)] for _ in range(num_rows)]

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1


def bfs():
    while q:
        row, col, num_breaks = q.popleft()
        if row == num_rows - 1 and col == num_cols - 1:
            return visited[row][col][num_breaks]

        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc

            if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
                if board[next_row][next_col] == 0 and visited[row][col][num_breaks] + 1 < visited[next_row][next_col][num_breaks]:
                    visited[next_row][next_col][num_breaks] = visited[row][col][num_breaks] + 1
                    q.append((next_row, next_col, num_breaks))

                if board[next_row][next_col] == 1 \
                        and num_breaks + 1 <= can_break \
                        and visited[row][col][num_breaks] + 1 < visited[next_row][next_col][num_breaks]:
                    visited[next_row][next_col][num_breaks + 1] = visited[row][col][num_breaks] + 1
                    q.append((next_row, next_col, num_breaks + 1))
    return -1

print(bfs())

