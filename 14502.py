import sys
from collections import deque
from copy import deepcopy

input = lambda: sys.stdin.readline().strip()
drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))

num_row, num_col = map(int, input().split())
max_area = 0

board = [list(map(int, input().split())) for i in range(num_row)]

def print_board(board):
    for line in board:
        print(' '.join(map(str, line)))
    print()


def bfs():
    temp_board = deepcopy(board)
    q = deque()
    
    for i in range(num_row):
        for j in range(num_col):
            if temp_board[i][j] == 2:
                q.append((i, j))
                
                
    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                continue
            
            if not temp_board[next_row][next_col]:
                temp_board[next_row][next_col] = 2
                q.append((next_row, next_col))
    
    cnt = 0
    
    for i in range(num_row):
        for j in range(num_col):
            if temp_board[i][j] == 0:
                cnt += 1
    
    return cnt
    
def dfs(cnt):
    global max_area
    if cnt == 3:
        ans = bfs()
        max_area = max(max_area, ans)
        
    else:
        for i in range(num_row):
            for j in range(num_col):
                if board[i][j] == 0:
                    board[i][j] = 1
                    dfs(cnt + 1)
                    board[i][j] = 0
dfs(0)

print(max_area)