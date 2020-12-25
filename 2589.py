from sys import stdin
from collections import deque


dxdy = [[-1, 0], [1, 0], [0, 1], [0, -1]]
maps = []
res = 0

num_row, num_col = map(int, input().split())
maps += [list(map(str, input())) for _ in range(num_row)]
    
queue = deque()

def bfs(row, col):
    global num_row
    global num_col
    global maps
    global queue
    max_val = 0
    distance = [[0] * num_col for _ in range(num_row)]
    
    
    queue.append((row, col))
    distance[row][col] = 1
    
    while queue:
        row, col = queue.popleft()
        
        for i in range(4):
            next_row = row + dxdy[i][0]
            next_col = col + dxdy[i][1]
            
            if 0 <= next_row < num_row and 0 <= next_col < num_col:
                if distance[next_row][next_col] == 0 and maps[next_row][next_col] == 'L':
                    distance[next_row][next_col] = distance[row][col] + 1
                    max_val = max(max_val, distance[next_row][next_col])
                    queue.append((next_row, next_col))

    return max_val - 1

for i in range(num_row):
    for j in range(num_col):
        if maps[i][j] == 'L':
            res = max(res, bfs(i, j))
        
print(res)