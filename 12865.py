import sys

input = lambda: sys.stdin.readline().strip()

num_stocks, max_weight = map(int, input().split())

stocks = [tuple(map(int, input().split())) for i in range(num_stocks)]
stocks = [0] + stocks
dp = [[0] * (max_weight + 1) for i in range(num_stocks + 1)]

for i in range(1, num_stocks + 1):
    for w in range(1, max_weight + 1):
        weight, value = stocks[i]

        if w < weight:
            dp[i][w] = dp[i - 1][w]
        else:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)


print(dp[num_stocks][max_weight])
