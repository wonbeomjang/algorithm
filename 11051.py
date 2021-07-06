import sys 
from itertools import combinations
input = lambda: sys.stdin.readline().strip()

N, K = map(int, input().split())

dp = [[1] * 1001 for i in range(1001)]

for i in range(2, 1001):
    for j in range(1, i):
        dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 10007

print(dp[N][K] % 10007)
