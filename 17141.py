from itertools import combinations
from collections import deque


drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))


n, num_virus = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]

virus = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus += [(i, j)]

def spread(virus):
    q = deque(list(virus))\

    visited = [[0] * n for _ in range(n)]
    for i, j in virus:
        visited[i][j] = 1

    while q:
        row, col = q.popleft()
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc

            if not (0 <= next_row < n and 0 <= next_col < n):
                continue

            if board[next_row][next_col] != 1 and not visited[next_row][next_col]:
                visited[next_row][next_col] = visited[row][col] + 1
                q.append((next_row, next_col))
    return visited


def result(visited, board):
    times = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] != 1:
                if not visited[i][j]:
                    return float('inf')
                times = max(times, visited[i][j])
    return times


answer = float('inf')

for virus_locations in combinations(virus, num_virus):
    visited = spread(virus_locations)
    spread_time = result(visited, board)

    answer = min(answer, spread_time)

if answer == float('inf'):
    print(-1)
else:
    print(answer - 1)



