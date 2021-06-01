import sys
input = lambda: sys.stdin.readline().strip()

str1 = input()
str2 = input()

len1 = len(str1)
len2 = len(str2)

dp = [[0] * (len2 + 1) for i in range(len1 + 1)]

for i, char1 in enumerate(str1, 1):
    for j, char2 in enumerate(str2, 1):
        if char1 == char2:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            
print(dp[len1][len2])

i = len1
j = len2
        
ans = ''

while dp[i][j]:
    if dp[i][j] == dp[i][j - 1]:
        j -= 1
    elif dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i-1][j-1] + 1:
        dp[i][j] == dp[i - 1][j - 1]
        ans = str1[i - 1] + ans
        i -= 1
        j -= 1
        
print(ans)