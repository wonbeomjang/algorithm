import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))

num_row, num_col = map(int, input().split())

board = [list(map(int, input().split())) for i in range(num_row)]
    
def check():
    visited = [[0] * num_col for i in range(num_row)]
    cnt = 0
    
    for i in range(num_row):
        for j in range(num_col):
            if board[i][j] == 1:
                cnt += 1
    return cnt

def bfs(q, visited):
    res = deque()
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                continue
            
            if not visited[next_row][next_col]:
                if not board[next_row][next_col]:
                    q.append((next_row, next_col))
                    visited[next_row][next_col] = True
                    
                else:
                    visited[next_row][next_col] = True
                    res.append((next_row, next_col))
                    
    return res
    
def get_q_visited():
    global num_row, num_col
        
    q = deque()
    visited = [[0] * num_col for i in range(num_row)]
    
    for i in range(num_row):
        visited[i][0] = True
        visited[i][num_col - 1] = True
        
        q.append((i, 0))
        q.append((i, num_col - 1))
        
    for i in range(num_col):
        visited[0][i] = True
        visited[num_row - 1][i] = True
        
        q.append((0, i))
        q.append((num_row - 1, i))
    
    return q, visited


chk = check()
ans = 0
cnt = 0

while chk:
    chk = check()
    
    if not chk:
        break
    cnt += 1
    ans = chk
    
    q, visited = get_q_visited()
    res = bfs(q, visited)
    
    for i in range(len(res)):
        row = res[i][0]
        col = res[i][1]
        
        board[row][col] = 0
    
print(cnt)
print(ans)