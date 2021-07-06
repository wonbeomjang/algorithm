import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
drdc = ((1, 0), (-1, 0), (0, -1), (0, 1))

board = [list(input()) for i in range(12)]

def bfs(row, col, visited):
    q = deque()
    res = deque()
    
    color = board[row][col]
    q.append((row, col))
    res.append((row, col))
    visited[row][col] = True
    
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < 12 and 0 <= next_col < 6):
                continue
            
            if not visited[next_row][next_col] and board[next_row][next_col] == color:
                visited[next_row][next_col] = True
                q.append((next_row, next_col))
                res.append((next_row, next_col))
                
    return res
    

def explsion(board, blocks):
    for block in blocks:
        while block:
            print(1)
            row, col = block.popleft()
            board[row][col] = '.'
        
def fall(board):
    for i in range(11, -1, -1):
        for j in range(5, -1, -1):
            if board[i][j] != '.':
                res = i
                
                for k in range(i, 12):
                    if board[k][j] == '.':
                        res = k
                
                if res != i:
                    board[res][j] = board[i][j]
                    board[i][j] = '.'
                
                
                        
    

def search(board):
    visited = [[0] * 6 for i in range(12)]
    res = []
    
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                block = bfs(i, j, visited)
                if len(block) >= 4:
                    res += [block]
    return res

ans = 0

while True:
    res = search(board)
    if not res: break
    ans += 1
    explsion(board, res)
    fall(board)

print(ans)

"""
......
......
......
......
......
......
......
......
.Y....
.YG...
RRYG..
RRYGG.

......
......
......
......
......
......
......
......
.Y....
.YG...
..YG..
..YGG.
"""
                    