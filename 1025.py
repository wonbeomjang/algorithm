import sys

input = lambda: sys.stdin.readline().strip()
num_row, num_col = map(int, input().split())

board = [list(input()) for i in range(num_row)]

answer = float('-inf')
for dr in range(-num_row, num_row):
    for dc in range(-num_col, num_col):
        for row in range(num_row):
            for col in range(num_col):
                if dr == dc == 0:
                    continue
                num = ""
                while 0 <= row < num_row and 0 <= col < num_col:
                    num += board[row][col]
                    row += dr
                    col += dc
                    if float(num) ** 0.5 % 1 == 0:
                        answer = max(answer, float(num))
print(-1 if answer == float('-inf') else int(answer))