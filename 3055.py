from collections import deque

drdc = [[1, 0], [-1, 0], [0, 1], [0, -1]]

num_row, num_col = map(int, input().split())

board = [list(input()) for _ in range(num_row)]
visited = [[0] * num_col for _ in range(num_row)]

hedgehog = None
water = []

marble = deque()
water = deque()

for i in range(num_row):
    for j in range(num_col):
        if board[i][j] == 'D':
            target_row, target_col = i, j
            
        elif board[i][j] == 'S':
            visited[i][j] = 1
            hedgehog = [i, j]
            marble.append([i, j])
        
        elif board[i][j] == '*':
            water.append([i, j])


while True:
    flag = False
    water_len = len(water)
    
    for i in range(water_len):
        row, col = water.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                continue
            
            if not board[next_row][next_col] == '*' and not board[next_row][next_col] == 'X' and not board[next_row][next_col] == 'D':
                board[next_row][next_col] = '*'
                water.append([next_row, next_col])
                
    
    marble_len = len(marble)
    
    for i in range(marble_len):
        row, col = marble.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                continue
            
            if board[next_row][next_col] != '*' and board[next_row][next_col] != 'X' and not visited[next_row][next_col]:
                visited[next_row][next_col] = visited[row][col] + 1
                marble.append([next_row, next_col])
                
    if not marble:
        print('KAKTUS')
        break
    
    if visited[target_row][target_col]:
        
        print(visited[target_row][target_col] - 1)
        break
    
