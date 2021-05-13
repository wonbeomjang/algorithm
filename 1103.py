import sys
from collections import deque

input = sys.stdin.readline
dxdy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
num_row, num_col = map(int, input().split())

board = [list(input())[:-1] for i in range(num_row)]
visited = [[False] * num_col for i in range(num_row)]
dp = [[-1] * num_col for i in range(num_row)]


def dfs(row, col):
    global visited, dp
    global board
    global dxdy
    global num_row, num_col
    
    if not (0 <= row < num_row and 0 <= col < num_col) or board[row][col] == 'H':
        return 0
        
    if visited[row][col]:
        return -1
        
    if dp[row][col] != -1:
        return dp[row][col]
    
    step_size = int(board[row][col])
    
    visited[row][col] = True
    for [dx, dy] in dxdy:
        next_row = row + step_size * dx
        next_col = col + step_size * dy
        
        val = dfs(next_row, next_col)
        if val != -1:
            dp[row][col] = max(dp[row][col], val + 1)
        else:
            return -1
    
    visited[row][col] = False
            
    return dp[row][col]
    
    
print(dfs(0, 0))


