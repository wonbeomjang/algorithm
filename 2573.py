from collections import deque
import sys
import copy

input = sys.stdin.readline
drdc = [[1, 0], [-1, 0], [0, 1], [0, -1]]

num_row, num_col = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(num_row)]


def bfs(row, col, visited):
    q = deque()
    q.append([row, col])
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col) or visited[next_row][next_col]:
                continue
            
            if board[next_row][next_col]:
                visited[next_row][next_col] = True
                q.append([next_row, next_col])

def melt(row, col):
    cnt = 0
    for dr, dc in drdc:
        next_row = row + dr
        next_col = col + dc
        
        if not (0 <= next_row < num_row and 0 <= next_col < num_col) or visited[next_row][next_col]:
            continue
        
        if not board[next_row][next_col]:
            cnt += 1
    
    return cnt

year = 0
while True:
    visited = [[False] * num_col for i in  range(num_row)]
    
    cnt = 0
    for i in range(num_row):
        for j in range(num_col):
            if not visited[i][j] and board[i][j]:
                bfs(i, j, visited)
                cnt += 1
    
    if cnt == 0:
        print(0)
        break
    elif cnt > 1:
        print(year)
        break
    
    temp_board = [[0] * num_col for _ in range(num_row)]
    for i in range(num_row):
        for j in range(num_col):
            if board[i][j]:
                temp_board[i][j] = max(board[i][j] - melt(i, j), 0)
    board = copy.deepcopy(temp_board)
    
    year += 1