from collections import deque

num_row, num_col = map(int, input().split())
board = [list(map(int, input())) for i in range(num_row)]
drdc = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(row, col, height, visited):
    global board
    global num_col, num_row
    
    water = [[0 for i in range(num_col)] for i in range(num_row)]
    water[row][col] = height - board[row][col]
    
    q = deque()
    
    visited[row][col] = True
    q.append([row, col])
    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                return False, []
                
            if visited[next_row][next_col]:
                continue
            
            if board[next_row][next_col] >= height:
                continue
            
            q.append([next_row, next_col])
            visited[next_row][next_col] = True
            
            water[next_row][next_col] = height - board[next_row][next_col]
            
    return True, water
    
    
    
max_val = 0
for i in range(num_row):
    max_val = max(max_val, *board[i])

ret = False
flag = False
res = 0
for height in range(max_val, -1, -1):
    if flag:
        for k in range(num_row):
            res += sum(water[k])
        break
    res = 0
    visited = [[False for i in range(num_col)] for i in range(num_row)]
    
    for i in range(num_row):
        for j in range(num_col):
            if height > board[i][j] and not visited[i][j]:
                if i == 1 and j == 1:
                    pass
                ret, water = bfs(i, j, height, visited)
                
                if not ret:
                    flag = True

print(res)