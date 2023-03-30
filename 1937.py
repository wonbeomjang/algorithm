import sys
sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().strip()
drdc = ((0, 1), (1, 0), (0, -1), (-1, 0))

num_row = num_col = int(input())
board = [list(map(int, input().split())) for i in range(num_row)]
dp = [[0] * num_col for i in range(num_row)]


def dfs(row, col):
    global board, dp, num_row, num_col

    if dp[row][col]:
        return dp[row][col]

    dp[row][col] = 1

    for dr, dc in drdc:
        next_row = row + dr
        next_col = col + dc

        if 0 <= next_row < num_row and 0 <= next_col < num_col and board[next_row][next_col] < board[row][col]:
            dp[row][col] = max(dp[row][col], dfs(next_row, next_col) + 1)

    return dp[row][col]


answer = 0
for i in range(num_row):
    for j in range(num_col):
        answer = max(answer, dfs(i, j))

print(answer)