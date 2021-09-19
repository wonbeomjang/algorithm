import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
path = [-1] *100001

def bfs(n, k):
    global path
    q = deque()
    q.append((n, 0))
    
    visited = [False] * 100001
    visited[n] = True
    
    while q:
        v, d = q.popleft()
        if v == k:
            return d
        
        for nv in (v - 1, v + 1, v * 2):
            if not 0 <= nv < 100001:
                continue
            
            if not visited[nv]:
                path[nv] = v
                visited[nv] = True
                q.append((nv, d + 1))
                
print(bfs(n, k))
res = []

v = k
while True:
    res += [v]
    
    if v == n: break
    v = path[v]

print(' '.join(map(str, reversed(res))))