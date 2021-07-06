import sys

input = lambda: sys.stdin.readline().strip()


dp = [[0 for i in range(10)] for j in range(102)]

for digit in range(1, 10):
    dp[1][digit] = 1

for i in range(2, 101):
    for digit in range(10):
        if digit > 0:
            dp[i][digit - 1] += dp[i - 1][digit]
        
        if digit < 9:
            dp[i][digit + 1] += dp[i - 1][digit]
        
        dp[i][digit - 1] %= 1000000000

length = int(input())
print(sum(dp[length]) % 1000000000)
    
"""
0 1
1 02
2 13
3 24
4 35
5 46
6 57
7 68
8 79
9 8
"""