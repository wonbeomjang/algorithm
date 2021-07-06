import sys

input = lambda: sys.stdin.readline().strip()

MAXTIME   = 1000
MAXHEALTH = 30
NUMTREE   = 2

max_time, max_health = map(int, input().split())

dp = [[[0] * (NUMTREE) for _ in range(MAXHEALTH + 2)] for _ in range(MAXTIME + 1)]

tree = int(input()) - 1
other = not tree

if tree == 0:
    dp[1][max_health][tree] = 1
    dp[1][max_health - 1][other] = 0
else:
    dp[1][max_health - 1][tree] = 1
    dp[1][max_health][other] = 0

for i in range(2, max_time + 1):
    tree = int(input()) - 1
    other = not tree
    
    for h in range(max_health + 1):
        dp[i][h][tree]  = max(dp[i - 1][h + 1][other], dp[i - 1][h][tree]) + 1
        dp[i][h][other] = max(dp[i - 1][h + 1][tree], dp[i - 1][h][other])

ans = 0
for sublist in dp[max_time]:
    ans = max((ans, *sublist))
print(ans)
    