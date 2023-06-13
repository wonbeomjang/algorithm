from collections import defaultdict, deque
from itertools import combinations

num_city = int(input())
populations = [0] + list(map(int, input().split()))
edge = defaultdict(list)


def bfs(cities: set):
    visited = set()
    q = deque([list(cities)[0]])
    visited.add(q[0])
    population = populations[q[0]]

    while q:
        cur_city = q.popleft()
        for next_city in edge[cur_city]:
            if next_city in cities and next_city not in visited:
                visited.add(next_city)
                q.append(next_city)
                population += populations[next_city]

    return len(visited) == len(cities), population


for i in range(1, num_city + 1):
    edge[i] = list(map(int, input().split()))[1:]

cities = set(range(1, num_city + 1))
min_gap = float('inf')

for i in range(1, num_city // 2 + 1):
    for combi in combinations(range(1, num_city + 1), i):
        combi = set(combi)
        div_1, pop_1 = bfs(combi)
        div_2, pop_2 = bfs(cities.difference(combi))

        if div_1 and div_2:
            min_gap = min(min_gap, abs(pop_1 - pop_2))

if min_gap == float('inf'):
    print(-1)
else:
    print(min_gap)





