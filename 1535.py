N = int(input())
loss = list(map(int, input().split()))
pleasure = list(map(int, input().split()))

loss = [0] + loss
pleasure = [0] + pleasure

hp = 100
happy = 0

dp = [[0 for i in range(101)] for j in range(21)]


for i in range(N + 1):
    for h in range(1, 101):
        dp[i][h] = dp[i - 1][h]
        if h > loss[i]:
            dp[i][h] = max(dp[i][h], dp[i - 1][h - loss[i]] + pleasure[i])
            
print(dp[N][99])