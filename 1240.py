from collections import deque

N, M = map(int, input().split())

edges = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    v1, v2, dis = map(int, input().split())
    edges[v1].append([v2, dis])
    edges[v2].append([v1, dis])
    
def bfs(v1, v2):
    global N
    q = deque()
    q.append([v1, 0])
    visited = [False for _ in range(N + 1)]
    
    while q:
        v, distance = q.popleft()
        
        if v == v2:
            return distance    
        
        for next_v, dis in edges[v]:
            if not visited[next_v]:
                visited[next_v] = True
                q.append([next_v, distance + dis])
    
    return 0
    
for _ in range(M):
    v1, v2 = map(int, input().split())
    print(bfs(v1, v2))
        