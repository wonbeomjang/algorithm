import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()
drdc = ((-1, 0), (0, -1), (0, 1), (1, 0))

num_row = num_col = int(input())
board = [list(map(int, input().split())) for i in range(num_row)]
shark_size = 2
num_eat = 0
row, col = 0, 0
time = 0


def search_shark():
    global row, col
    for i in range(num_row):
        for j in range(num_col):
            if board[i][j] == 9:
                row = i
                col = j
                board[i][j] = 0
                return


def bfs():
    global board, shark_size, row, col, num_row, num_col
    visited = [[0] * num_col for i in range(num_row)]

    q = deque()
    q.append((row, col))
    visited[row][col] = 1
    eat = []

    while q:
        row, col = q.popleft()

        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            if not (0 <= next_row < num_row and 0 <= next_col < num_col) or visited[next_row][next_col]:
                continue

            if board[next_row][next_col] <= shark_size:
                visited[next_row][next_col] = visited[row][col] + 1
                q.append((next_row, next_col))

                if 0 < board[next_row][next_col] < shark_size:
                    eat += [(visited[next_row][next_col] - 1, next_row, next_col)]

    if eat:
        eat.sort()
        t, row, col = eat[0]
        board[row][col] = 0
        return t
    return 0


search_shark()

while result := bfs():
    num_eat += 1
    time += result
    if shark_size == num_eat:
        num_eat = 0
        shark_size += 1

print(time)