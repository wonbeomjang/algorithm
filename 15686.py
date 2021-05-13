from collections import deque

drdc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    global board
    global N
    
    visited = [[False] * N for _ in range(N)]
    q = deque()
    res = 0
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                q.append([i, j, 0])
                visited[i][j] = True
    
    
    while q:
        row, col, dis = q.popleft()
        
        if board[row][col] == 1:
            res += dis
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < N and 0 <= next_col < N):
                continue
            
            if not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                q.append([next_row, next_col, dis + 1])
    
    return res

remain_store = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            remain_store += 1

def close(remain):
    global board
    if remain <= M:
        close.answer = min(bfs(), close.answer)
        return close.answer
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                board[i][j] = 0
                close(remain - 1)
                board[i][j] = 2
    
    return close.answer

close.answer = float('inf')

print(close(remain_store))
