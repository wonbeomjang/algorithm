import copy
from itertools import permutations


num_row, num_col, num_rotate = map(int, input().split())
board = [list(map(int, input().split())) for i in range(num_row)]
rotate_ops = [list(map(int, input().split())) for i in range(num_rotate)]


def rotate(board, r, c, s):
    result = copy.deepcopy(board)
    for d in range(1, s + 1):
        for j in range(c - d + 1, c + d + 1):
            result[r - d][j] = board[r - d][j - 1]

        for j in range(c - d, c + d):
            result[r + d][j] = board[r + d][j + 1]

        for i in range(r - d, r + d):
            result[i][c - d] = board[i + 1][c - d]

        for i in range(r - d + 1, r + d + 1):
            result[i][c + d] = board[i - 1][c + d]
    return result


def calc(board):
    res = float('inf')
    for line in board:
        res = min(res, sum(line))
    return res

answer = float('inf')
for orders in permutations(range(len(rotate_ops)), len(rotate_ops)):
    temp = copy.deepcopy(board)
    for order in orders:
        r, c, s = rotate_ops[order]
        temp = rotate(temp, r - 1, c - 1, s)
    answer = min(answer, calc(temp))

print(answer)
