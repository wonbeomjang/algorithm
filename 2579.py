import sys

input = lambda: sys.stdin.readline().strip()

num_stairs = int(input())

stairs = [0 for i in range(num_stairs + 2)]
dp = [0 for i in range(num_stairs + 2)]

for i in range(1, num_stairs + 1):
    stairs[i] = int(input())
    
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, num_stairs + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]

print(dp[num_stairs])