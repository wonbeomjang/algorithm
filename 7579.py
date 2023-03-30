import sys

input = lambda: sys.stdin.readline().strip()


N, M = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
cost_sum = sum(cost)
dp = [[0] * (cost_sum + 1) for i in range(N + 1)]
result = cost_sum

for i in range(1, N + 1):
    for c in range(1, cost_sum + 1):
        if c < cost[i]:
            dp[i][c] = dp[i - 1][c]
        else:
            dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - cost[i]] + memory[i])

        if dp[i][c] >= M:
            result = min(result, c)

if M:
    print(result)
else:
    print(0)
