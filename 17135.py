import copy
import sys
import heapq
from itertools import combinations


input = lambda: sys.stdin.readline().strip()
drdc = ((0, -1), (-1, 0), (0, 1))

num_row, num_col, max_distance = map(int, input().split())
board = [list(map(int, input().split())) for i in range(num_row)]


def print_board(board):
    for line in board:
        print(" ".join(map(str, line)))
    print()


def move(board):
    for i in range(num_row - 1, 0, -1):
        for j in range(num_col):
            board[i][j] = board[i - 1][j]

    for j in range(num_col):
        board[0][j] = 0


def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def kill(board, shooter):
    cnt = 0
    kill_info = [[], [], []]

    for i in range(num_row):
        for j in range(num_col):
            if board[i][j] == 1:
                for s in range(3):
                    heapq.heappush(kill_info[s], ((get_distance(shooter[s], (i, j)), j), i, j))

    for s in range(3):
        if kill_info[s]:
            (d, _), i, j = heapq.heappop(kill_info[s])

            if d <= max_distance and board[i][j] == 1:
                cnt += 1
                board[i][j] = 0

    return cnt


answer = 0
temp = copy.deepcopy(board)

for p1, p2, p3 in combinations(range(num_col), 3):
    shooter = [(num_row, p1), (num_row, p2), (num_row, p3)]
    cur_score = 0
    board = copy.deepcopy(temp)
    for i in range(num_row):
        cur_score += kill(board, shooter)
        move(board)
    answer = max(answer, cur_score)

# shooter = [(5, 0), (5, 1), (5, 3)]
# cur_score = 0
# for i in range(num_row):
#     cur_score += kill(board, shooter)
#     print_board(board)
#     move(board)
# print(cur_score)


print(answer)