from collections import deque

num_row = num_col = int(input())
board = [list(map(int, input().split())) for i in range(num_row)]
dp = [[[0] * 3 for i in range(num_col)] for i in range(num_row)]

# dp[num_row - 1][num_col - 1] = [1, 1, 1]
dp[0][1][0] = 1

drdcrot = {
    0: ((0, -1, 0), (0, -1, 1)),
    1: ((-1, -1, 0), (-1, -1, 1), (-1, -1, 2)),
    2: ((-1, 0, 2), (-1, 0, 1))
}


def dfs(row, col, rot):
    if dp[row][col][rot]:
        return dp[row][col][rot]

    res = 0
    for dr, dc, next_rot in drdcrot[rot]:
        next_row = row + dr
        next_col = col + dc

        if next_rot == 0:
            if not (0 <= next_row and 0 <= next_col - 1):
                continue
            if board[next_row][next_col] or board[next_row][next_col - 1]:
                continue
        if next_rot == 1:
            if not (0 <= next_row - 1 and 0 <= next_col - 1):
                continue
            if board[next_row][next_col] or board[next_row][next_col - 1] or board[next_row - 1][next_col - 1] or board[next_row - 1][next_col]:
                continue
        if next_rot == 2:
            if not (0 <= next_row - 1 and 0 <= next_col):
                continue
            if board[next_row][next_col] or board[next_row - 1][next_col]:
                continue
        res += dfs(next_row, next_col, next_rot)
    dp[row][col][rot] = res
    return res


if not (board[num_row - 1][num_col - 1] or board[num_row - 1][num_col - 2]):
    dfs(num_row - 1, num_col - 1, 0)
if not (board[num_row - 1][num_col - 1] or board[num_row - 1][num_col - 2] or board[num_row - 2][num_col - 1] or board[num_row - 2][num_col - 2]):
    dfs(num_row - 1, num_col - 1, 1)
if not (board[num_row - 1][num_col - 1] or board[num_row - 2][num_col - 1]):
    dfs(num_row - 1, num_col - 1, 2)

print(sum(dp[num_row - 1][num_col - 1]))