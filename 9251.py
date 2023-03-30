str1 = input()
str2 = input()

dp = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] != str2[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        else:
            dp[i + 1][j + 1] = dp[i][j] + 1

print(dp[-1][-1])
