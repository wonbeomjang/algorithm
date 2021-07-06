import sys

input = lambda: sys.stdin.readline().strip()

num_stone = int(input())

player = {'SK': True, 'CY': False}
dp = [0 for i in range(1001)]

dp[0] = player['SK']
dp[1] = player['SK']
dp[2] = player['CY']
dp[3] = player['SK']

for i in range(4, 1001):
    dp[i] = not dp[i - 1]
    dp[i] = not dp[i - 3]
    
print('SK' if dp[num_stone] else 'CY')