import sys
from copy import deepcopy
from itertools import chain
from collections import deque

input = lambda: sys.stdin.readline().strip()
drdc = ((-1, 0), (1, 0), (0, -1), (0, 1))

n, num_firestorm = map(int, input().split())
n = 2 ** n
board = [list(map(int, input().split())) for i in range(n)]
stages = list(map(int, input().split()))

def print_board():
    global board
    print()
    for line in board:
        print(' '.join(map(str, line)))

def rotate(stage):
    global board
    
    k = 2 ** stage
    
    for r in range(0, n, k):
        for c in range(0, n, k):
            origin = [board[i][c:c+k] for i in range(r, r + k)]
            for i in range(k):
                for j in range(k):
                    board[r + j][c + k - 1 - i] = origin[i][j]

def melt():
    global board
    
    temp_board = deepcopy(board)
    for row in range(n):
        for col in range(n):
            if not temp_board[row][col]:
                continue
            
            cnt = 0
            for dr, dc in drdc:
                next_row, next_col = row + dr, col + dc
                if (0 <= next_row < n and 0 <= next_col < n) and board[next_row][next_col]:
                    cnt += 1
            
            if cnt < 3:
                temp_board[row][col] -= 1
    board = temp_board

def bfs(row, col, visited):
    global board
    q = deque()
    
    q.append((row, col))
    visited[row][col] = True
    cnt = 1
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < n and 0 <= next_col < n):
                continue
            
            if not visited[next_row][next_col] and board[next_row][next_col]:
                cnt += 1
                q.append((next_row, next_col))
                visited[next_row][next_col] = True
    
    return cnt

for l in stages:
    rotate(l)
    melt()
    
print(sum(chain(*board)))

max_ans = 0
visited = [[False] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] and not visited[i][j]:\
            max_ans = max(max_ans, bfs(i, j, visited))
print(max_ans)