import heapq

num_vertices, num_edges = map(int, input().split())
start_vertex = int(input())

edges = [[] for _ in range(num_vertices + 1)]

for _ in range(num_edges):
    v1, v2, weight = map(int, input().split())
    edges[v1].append([v2, weight])

distance = [float('INF') for _ in range(num_vertices + 1)]
visited = [False for _ in range(num_vertices + 1)]
distance[start_vertex] = 0

q = []

heapq.heappush(q, [0, start_vertex])

while q:
    w, v = heapq.heappop(q)
    
    for nv, w in edges[v]:
        
        if distance[v] + w < distance[nv]:
            distance[nv] = distance[v] + w
            q.append([distance[nv], nv])

for i in range(1, num_vertices + 1):
    print(distance[i] if isinstance(distance[i], int) else 'INF')
    