from collections import deque
import sys

input = sys.stdin.readline

drdx = [[0, -1], [-1, 0], [0, 1], [1, 0]]

WEST = 1
NORTH = 2
EAST = 4
SOUTH = 8

num_col, num_row = map(int, input().split())

wall = [list(map(int, input().split())) for _ in range(num_row)]

def bfs(row, col, visited):
    global num_row, num_col
    
    q = deque()
    q.append([row, col])
    visited[row][col] = True
    cnt = 1
    
    while q:
        row, col = q.popleft()
        bit = 1
        for dr, dc in drdx:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                bit = bit << 1
                continue
            
            if not (wall[row][col] & bit) and not visited[next_row][next_col]:
                q.append([next_row, next_col])
                visited[next_row][next_col] = True
                cnt += 1
                
            bit = bit << 1
            
    return cnt
    
cnt = 0
max_home = 0
visited = [[False] * num_col for _ in range(num_row)]

for i in range(num_row):
    for j in range(num_col):
        if not visited[i][j]:
            max_home = max(bfs(i, j, visited), max_home)
            cnt += 1
            
print(cnt)
print(max_home)

for i in range(num_row):
    for j in range(num_col):
        for s in range(4):
            if wall[i][j] & 1 << s:
                visited = [[False] * num_col for _ in range(num_row)]
                
                wall[i][j] -= 1 << s
                max_home = max(bfs(i, j, visited), max_home)
                wall[i][j] += 1 << s

print(max_home)