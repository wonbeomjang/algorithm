import sys

input = lambda: sys.stdin.readline().strip()

num_row, num_col = map(int, input().split())

board = [[0] * (num_col + 1) for i in range(num_row + 1)]
dp = [[0] * (num_col + 1) for i in range(num_row + 1)]

ans = 0

for i in range(1, num_row + 1):
    line = list(input())
    
    for j in range(1, num_col + 1):
        dp[i][j] = int(line[j - 1])
        if dp[i][j]:
            ans = 1
    
for i in range(1, num_row + 1):
    for j in range(1, num_col + 1):
        if dp[i][j] and dp[i - 1][j] and dp[i][j - 1] and dp[i - 1][j - 1]:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            ans = max(ans, dp[i][j])

print(ans * ans)