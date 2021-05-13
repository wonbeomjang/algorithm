import sys
import heapq

input = sys.stdin.readline
num_cities, num_roads, num_pave = map(int, input().split())

INF = float('inf')

graph = [[] for _ in range(num_cities + 1)]

for _ in range(num_roads):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((cost, v2))
    graph[v2].append((cost, v1))



hq = []
times = [[INF] * (num_pave + 1) for _ in range(num_cities + 1)]

for i in range(num_pave + 1):
    times[1][i] = 0
    
# cost, city, pave
heapq.heappush(hq, [0, 1, 0])
    
while hq:
    cur_cost, cur_city, cur_pave = heapq.heappop(hq)
    
    if times[cur_city][cur_pave] < cur_cost:
        continue
    
    for cost, next_city in graph[cur_city]:
        move_cost = cur_cost + cost
        
        if move_cost < times[next_city][cur_pave]:
            times[next_city][cur_pave] = move_cost
            heapq.heappush(hq, (move_cost, next_city, cur_pave))
        
        if cur_pave < num_pave and cur_cost < times[next_city][cur_pave + 1]:
            times[next_city][cur_pave + 1] = cur_cost
            heapq.heappush(hq, (cur_cost, next_city, cur_pave + 1))
    
    
print(min(times[num_cities]))