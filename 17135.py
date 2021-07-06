import sys
import heapq
from copy import deepcopy
from itertools import combinations

input = lambda: sys.stdin.readline().strip()

num_row, num_col, distance = map(int, input().split())
board = [list(map(int, input().split())) for i in range(num_row)]

def down(board):
    for i in range(num_row - 1, 0, -1):
        for j in range(num_col):
            board[i][j] = board[i - 1][j]
            
    for j in range(num_col):
        board[0][j] = 0

def get_distance(enamy, shooter):
    return abs(enamy[0] - shooter[0]) + abs(enamy[1] - shooter[1])

def shoot(board, positions, distance):
    shooters = [[], [], []]
    
    for i in range(num_row - 1, -1, -1):
        for j in range(num_col):
            for s in range(3):
                # (distance, col), row, col
                if board[i][j]:
                    heapq.heappush(shooters[s], ((get_distance(positions[s], (i, j)), j), i, j))
    cnt = 0

    for shooter in shooters:
        if shooter:
            (d, _), i, j = heapq.heappop(shooter)
            if d <= distance and board[i][j]:
                board[i][j] = 0
                cnt += 1
            
    return cnt
        

def print_board(board):
    print()
    for subline in board:
        print(' '.join(map(str, subline)))

def play(board, positions, distance):
    global num_row, num_col
    
    cnt = 0
    for i in range(num_row):
        cnt += shoot(board, positions, distance)
        down(board)
        
    return cnt

# positions = [(num_row, 0), (num_row, 2), (num_row, 4)]

# shoot(board, positions, distance)
# print_board(board)

ans = 0
for p1, p2, p3 in combinations(range(num_col), 3):
    positions = [(num_row, p1), (num_row, p2), (num_row, p3)]
    result = play(deepcopy(board), positions, distance)
    # print(p1, p2, p3, result)
    ans = max(ans, result)
    
print(ans)
    
    