import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

num_vertices, num_edges = map(int, input().split())

graph = [[] for _ in range(num_vertices + 1)] 

for _ in range(num_edges):
    v1, v2, cost = map(int, input().split())
    
    graph[v1] += [[v2, cost]]
    graph[v2] += [[v1, cost]]

ob_vertex_1, ob_vertex_2 = map(int, input().split())

def dijkstra(start):
    hq = []
    min_cost = [INF] * (num_vertices + 1)
    min_cost[start] = 0
        
    # cur_cost, cur_city, cur_state
    heapq.heappush(hq, [0, start])
    
    while hq:
        cur_cost, cur_city = heapq.heappop(hq)
        
        for next_city, cost in graph[cur_city]:
            next_cost = cur_cost + cost
            
            if next_cost < min_cost[next_city]:
                min_cost[next_city] = next_cost
                heapq.heappush(hq, [next_cost, next_city])
        
        
    return min_cost

start = dijkstra(1)
v1 = dijkstra(ob_vertex_1)
v2 = dijkstra(ob_vertex_2)

cnt = min(start[ob_vertex_1] + v1[ob_vertex_2] + v2[num_vertices], start[ob_vertex_2] + v2[ob_vertex_1] + v1[num_vertices])

print(cnt if cnt < INF else -1)                