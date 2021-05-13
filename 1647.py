import heapq
import sys

input = sys.stdin.readline

def prim(graph, num_houses):
    hq = []
    visited = [False] * (num_houses + 1)
    visited[1] = True
    costs = [0] * (num_houses + 1)
    i = 1
    
    for g in graph[1]:
        heapq.heappush(hq, g)
        
    while hq:
        cost, vertex = heapq.heappop(hq)
        
        if not visited[vertex]:
            visited[vertex] = True
            i += 1
            costs[vertex] += cost
            
            for g in graph[vertex]:
                heapq.heappush(hq, g)
            
        if i == num_houses:
            return sum(costs) - max(costs)
    
    return 0
    



def solution():
    
    num_houses, num_roads = map(int, input().split())
    
    graph = [[] for _ in range(num_houses + 1)]
    for _ in range(num_roads):
        A, B, C = map(int, sys.stdin.readline().split())
        graph[A].append([C, B])
        graph[B].append([C, A])
        
    print(prim(graph, num_houses))

solution()