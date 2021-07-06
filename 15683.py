import sys
from copy import deepcopy

input = lambda: sys.stdin.readline().strip()

num_row, num_col = map(int, input().split())

board = [list(map(int, input().split())) for i in range(num_row)]

drdc = ((-1, 0), (0, 1), (1, 0), (0, -1))

NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3

cctv = []
cctv5 = []

def move(row, col, board, direction):
    dr, dc = drdc[direction]
    
    while True:
        row += dr
        col += dc
        if not (0 <= row < num_row and 0 <= col < num_col):
            break
        
        if board[row][col] == 6:
            return
        
        elif board[row][col] == 0:
            board[row][col] = 9
            
def look(row, col, board, cctv_type, direction):
    if cctv_type == 1:
        move(row, col, board, direction)
        
    elif cctv_type == 2:
        move(row, col, board, direction)
        move(row, col, board, (direction + 2) % 4)
        
    elif cctv_type == 3:
        move(row, col, board, direction)
        move(row, col, board, (direction + 3) % 4)
        
    elif cctv_type == 4:
        move(row, col, board, direction)
        move(row, col, board, (direction + 2) % 4)
        move(row, col, board, (direction + 3) % 4)
        
    return board

def print_board(board):
    print()
    for subline in board:
        print(' '.join(map(str, subline)))

for i in range(num_row):
    for j in range(num_col):
        if 0 < board[i][j] < 5:
            cctv += [(i, j, board[i][j])]
            
        elif board[i][j] == 5:
            move(i, j, board, NORTH)
            move(i, j, board, EAST)
            move(i, j, board, SOUTH)
            move(i, j, board, WEST)

def count_zero(board):
    cnt = 0
    
    for i in range(num_row):
        for j in range(num_col):
            if board[i][j] == 0:
                cnt += 1
    
    return cnt

ans = float('inf')

def dfs(board, cnt):
    global cctv, ans
    if cnt == len(cctv):
        # print_board(board)
        ans = min(ans, count_zero(board))
        return
    
    for direction in range(4):
        temp = deepcopy(board)
        row, col, cctv_type = cctv[cnt]
        look(row, col, temp, cctv_type, direction)
        dfs(temp, cnt + 1)
    

dfs(board, 0)

print(ans)
            
