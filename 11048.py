import sys

input = lambda: sys.stdin.readline().strip()
drdc = ((1, 0), (0, 1), (1, 1))

num_row, num_col = map(int, input().split())

dp = [[0] * (num_col + 1) for i in range(num_row + 1)]
board = [list(map(int, input().split())) for i in range(num_row)]

for i in range(num_row):
    for j in range(num_col):
        dp[i + 1][j + 1] = board[i][j] + max((dp[i + 1][j], dp[i][j + 1], dp[i][j]))

print(dp[num_row][num_col])