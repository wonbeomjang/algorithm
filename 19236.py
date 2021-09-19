import sys
from copy import deepcopy

input = lambda: sys.stdin.readline().strip()

drdc = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
board = [[0] * 4 for i in range(4)]
fish = {}

for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        num, diretion = temp[2 * j], temp[2 * j + 1] - 1
        fish[num] = [i, j]
        board[i][j] = [num, diretion]
        
def move(srow, scol):
    global board, fish
    
    for i in range(1, 17):
        if not i in fish:
            continue
        
        row, col = fish[i]
        
        for _ in range(9):
            next_row = row + drdc[board[row][col][1]][0]
            next_col = col + drdc[board[row][col][1]][1]
            
            if not (0 <= next_row < 4 and 0 <= next_col < 4) or (next_row == srow and next_col == scol):
                board[row][col][1] = (board[row][col][1] + 1) % 8
                continue
            
            if not board[next_row][next_col]:
                fish[i] = [next_row, next_col]                
                board[row][col], board[next_row][next_col] = board[next_row][next_col], board[row][col]
            else:
                target_num = board[next_row][next_col][0]
                fish[i], fish[target_num] = fish[target_num], fish[i]
                board[row][col], board[next_row][next_col] = board[next_row][next_col], board[row][col]
            break
        
def eat(board, row, col):
    global fish
    
    num, direction = board[row][col]
    del fish[num]
    board[row][col] = []
        
    return num, direction
    

def print_board(index = 0):
    global board
    print()
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                print(f'{board[i][j][index]: 3}', end='')
            else:
                print(f'{-1: 3}', end='')
        print()

max_ans = 0
def dfs(row, col, direction, ans):
    global board, fish, max_ans
    move(row, col)
    
    while True:
        row += drdc[direction][0]
        col += drdc[direction][1]
        
        if not (0 <= row < 4 and 0 <= col < 4):
            max_ans = max(max_ans, ans)
            return
        
        if not board[row][col]:
            continue
        
        temp_board = deepcopy(board)
        temp_fish = deepcopy(fish)
        temp = board[row][col]
        
        eat(board, row, col)
        
        # num, direction = eat(row, col)
        dfs(row, col, temp[1], ans + temp[0])
        
        board = temp_board
        fish = temp_fish
        
row, col = 0, 0
num, direction = eat(board, row, col)
dfs(row, col, direction, num)
print(max_ans)