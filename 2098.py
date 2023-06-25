num_cities = int(input())
edge = {}

for i in range(num_cities):
    edge[i] = list(map(int, input().split()))
dp = [[float('inf')] * (1 << num_cities) for i in range(num_cities)]
ALL_VISITED = (1 << num_cities) - 1


def tsp(city, visited):
    if visited == ALL_VISITED:
        dp[city][visited] = edge[city][0]
        return edge[city][0]

    if dp[city][visited] != float('inf'):
        return dp[city][visited]

    for next_city in range(num_cities):
        if not edge[city][next_city]:
            continue
        if visited & (1 << next_city):
            continue
        dp[city][visited] = min(dp[city][visited], tsp(next_city, visited | (1 << next_city)) + edge[city][next_city])
    return dp[city][visited]

print(tsp(0, 1))
