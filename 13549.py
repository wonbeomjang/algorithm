import sys 
from collections import deque

input = lambda: sys.stdin.readline().strip()

MAXNUM = 100001
N, K = map(int, input().split())

q = deque()
visited = [0] * MAXNUM

q.append(N)
visited[N] = 1

while q:
    p = q.popleft()
    
    for n_p in (2 * p, p - 1, p + 1):
        if 0 <= n_p < MAXNUM and not visited[n_p]:
            q.append(n_p)
            
            if n_p == 2 * p:
                visited[n_p] = visited[p]
            else:
                visited[n_p] = visited[p] + 1
                
            
        
    
print(visited[K] - 1)