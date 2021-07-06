import sys
from collections import deque
from itertools import combinations

input = lambda: sys.stdin.readline().strip()
drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))

n, num_activate = map(int, input().split())

board = [list(map(int, input().split())) for i in range(n)]
viruses = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            viruses += [(i, j)]

num_virus = len(viruses)    
            
def count_max(visited):
    max_num = 0
    
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                if visited[i][j]:
                    max_num = max(max_num, visited[i][j])
                else:
                    return float('inf')
    
    return max_num - 1
    
    
def spread(q, visited):
    global board
    max_time = 0
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < n and 0 <= next_col < n):
                continue
            
            if not visited[next_row][next_col] and board[next_row][next_col] != 1:
                visited[next_row][next_col] = visited[row][col] + 1
                q.append((next_row, next_col))
    
    return visited
    
ans = float('inf')

for vs in combinations(range(num_virus), num_activate):
    q = deque()
    visited = [[0] * n for i in range(n)]
    
    for v in vs:
        row, col = viruses[v]
        visited[row][col] = 1
        q.append((row, col))
    
    visited = spread(q, visited)
    res = count_max(visited)
    ans = min(ans, res)

if ans == float('inf'):
    print(-1)
elif ans == -1:
    print(0)
else:
    print(ans)
    