dp = [False] * 20001
for i in range(1, 10001):
    dp[sum(map(int, list(f'{i}')))+i] = True

for i in range(1, 10001):
    if not dp[i]:
        print(i)