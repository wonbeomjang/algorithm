from collections import deque

dhdrdc = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

num_height, num_row, num_col = 0, 0, 0
board = []
ans = []

def bfs(height, row, col):
    global num_height, num_row, num_col
    global board
    global start_height, start_row, start_col
    global target_height, target_row, target_col
    global ans
    
    visited = [[[0] * num_col for _ in range(num_row)] for _ in range(num_height)]
    visited[height][row][col] = 1
    
    q = deque()
    q.append([height, row, col])
    
    while q:
        height, row, col = q.popleft()
        if height == target_height and row == target_row and col == target_col:
            ans += [f'Escaped in {visited[target_height][target_row][target_col] - 1} minute(s).']
            break
        
        for dh, dr, dc in dhdrdc:
            next_height = height + dh
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_height < num_height and 0 <= next_row < num_row and 0 <= next_col < num_col) or visited[next_height][next_row][next_col]:
                continue
            
            if board[next_height][next_row][next_col] != '#':
                q.append([next_height, next_row, next_col])
                visited[next_height][next_row][next_col] = visited[height][row][col] + 1
                
    else:
        ans += ['Trapped!']
    

while True:
    board = []
    num_height, num_row, num_col = map(int, input().split())
    
    if not num_height:
        break
    
    for _ in range(num_height):
        board += [[list(input()) for i in range(num_row)]]
        input()
    
    for i in range(num_height):
        for j in range(num_row):
            for k in range(num_col):
                if board[i][j][k] == 'S':
                    start_height, start_row, start_col = i, j, k
                elif board[i][j][k] == 'E':
                    target_height, target_row, target_col = i, j, k
    
    bfs(start_height, start_row, start_col)
for answer in ans:
    print(answer)
