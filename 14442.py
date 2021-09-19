import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
drdc = ((-1, 0), (0, 1), (1, 0), (0, -1))

num_row, num_col, num_wall = map(int, input().split())

board = [list(map(int, list(input()))) for i in range(num_row)]
visited = [[[0] * (num_wall + 1) for i in range(num_col)] for i in range(num_row)]

def bfs(visited):
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    
    while q:
        row, col, cnt = q.popleft()
        
        if row == num_row - 1 and col == num_col - 1:
            return visited[row][col][cnt]
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                continue
            
            if not visited[next_row][next_col][cnt]:
                
                if not board[next_row][next_col]:
                    visited[next_row][next_col][cnt] = visited[row][col][cnt] + 1
                    q.append((next_row, next_col, cnt))
                
                elif cnt < num_wall:
                    visited[next_row][next_col][cnt + 1] = visited[row][col][cnt] + 1
                    q.append((next_row, next_col, cnt + 1))
    return -1
                
print(bfs(visited))