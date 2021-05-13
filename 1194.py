from collections import deque

num_row, num_col = map(int, input().split())
drdc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
board = [list(input()) for i in range(num_row)]

for i in range(num_row):
    for j in range(num_col):
        if board[i][j] == '0':
            start_pos = [i, j]
            

def bfs(row, col):
    visited = [[[False for _ in range(num_col)] for _ in range(num_row)] for _ in range(1 << 6)]
    q = deque()
    visited[0][row][col] = True
    q.append([row, col, 0, 0])
    
    while q:
        row, col, cnt, key = q.popleft()
        
        if board[row][col] == '1':
                        return cnt
                        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if 0 <= next_row < num_row and 0 <= next_col < num_col:
                if not board[next_row][next_col] == '#' and not visited[key][next_row][next_col]:
                    
                    
                    if 'a' <= board[next_row][next_col] <= 'f':
                        new_key = key | 1 << (ord(board[next_row][next_col]) - ord('a'))
            
                        if not visited[new_key][next_row][next_col]:
                            visited[new_key][next_row][next_col] = True
                            visited[key][next_row][next_col] = True
                            q.append([next_row, next_col, cnt + 1, new_key])
                        
                    elif 'A' <= board[next_row][next_col] <= 'F':
                        if key & (1 << (ord(board[next_row][next_col]) - ord('A'))):
                            visited[key][next_row][next_col] = True
                            q.append([next_row, next_col, cnt + 1, key])
                    
                    else:
                        visited[key][next_row][next_col] = True
                        q.append([next_row, next_col, cnt + 1, key])
    return -1
    
print(bfs(*start_pos))