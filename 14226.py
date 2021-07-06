import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))

n, left, right = map(int, input().split())

board = [list(map(int, input().split())) for i in range(n)]

def bfs(row, col, visited):
    global left, right, board
    
    q = deque()
    q.append((row, col))
    temp = [(row, col)]
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < n and 0 <= next_col < n):
                continue
            
            if not visited[next_row][next_col] and left <= abs(board[next_row][next_col] - board[row][col]) <= right:
                visited[next_row][next_col] = True
                q.append((next_row, next_col))
                temp.append((next_row, next_col))
                
    return temp

num_move = 0

while True:
    visited = [[False] * n for i in range(n)]
    flag = False
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                temp = bfs(i, j, visited)
                
                if len(temp) > 1:
                    flag = True
                    val = sum((board[i][j] for (i, j) in temp)) // len(temp)
                    
                    for row, col in temp:
                        board[row][col] = val
    
    if not flag:
        break
    
    num_move += 1
    
print(num_move)
                    
    
