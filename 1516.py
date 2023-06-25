from collections import defaultdict

num_buildings = int(input())
prev = {}
time = {}

for i in range(1, num_buildings + 1):
    inputs = list(map(int, input().split()))
    prev[i] = inputs[1:-1]
    time[i] = inputs[0]


dp = [0] * (num_buildings + 1)


def dfs(i):
    if dp[i] != 0:
        return dp[i]
    max_time = time[i]
    for v in prev[i]:
        max_time = max(max_time, dfs(v) + time[i])

    dp[i] = max_time
    return max_time


for i in range(1, num_buildings + 1):
    print(dfs(i))
