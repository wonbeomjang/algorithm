import sys

input = lambda: sys.stdin.readline().strip()

str1 = input()
str2 = input()
str3 = input()

len1 = len(str1)
len2 = len(str2)
len3 = len(str3)

dp = [[[0] * (len3 + 1) for _ in range(len2 + 1)] for _ in range(len1 + 1)]

for i, char1 in enumerate(str1, 1):
    for j, char2 in enumerate(str2, 1):
        for k, char3 in enumerate(str3, 1):
            if char1 == char2 == char3:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

print(dp[len1][len2][len3])
