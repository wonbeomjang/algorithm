from operator import itemgetter
import heapq

num_vertices, num_edges = map(int, input().split())

adj = [[] for i in range(num_vertices + 1)]

def prim(start):
    global num_vertices
    q = []
    visited = [False] * (num_vertices + 1)
    visited[start] = True
    total_weight = 0
    cnt = 1
    
    for v in adj[start]:
        heapq.heappush(q, v)
        
    while q:
        weight, v = heapq.heappop(q)
        
        if not visited[v]:
            visited[v] = True
            cnt += 1
            total_weight += weight
            for a in adj[v]:
                heapq.heappush(q, a)
        
        if cnt == num_vertices:
            return total_weight
    else:
        return 0

for i in range(num_edges):
    v1, v2, weight = map(int, input().split())
    adj[v1] += [[weight, v2]]
    adj[v2] += [[weight, v1]]

print(prim(1))