import sys

input = lambda: sys.stdin.readline().strip()
MAXNUM = 100001

dp = [float('inf') for i in range(MAXNUM)]

dp[2] = 1
dp[5] = 1

for i in range(1, MAXNUM):
    if dp[i] != float('inf'):
        # print(i, dp[i])
        if i + 5 < MAXNUM and dp[i + 5] > dp[i] + 1:
            dp[i + 5] = dp[i] + 1
        if i + 2 < MAXNUM and dp[i + 2] > dp[i] + 1:
            dp[i + 2] = dp[i] + 1
        
n = int(input())
print(-1 if dp[n] == float('inf') else dp[n])
# for i in range(MAXNUM):
    # print(f'{i} {dp[i]}')