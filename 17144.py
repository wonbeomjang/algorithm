import sys
from collections import deque

drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))

input = lambda: sys.stdin.readline().strip()

num_row, num_col, time = map(int, input().split())

def spread(board):
    q = deque()
    
    for i in range(num_row):
        for j in range(num_col):
            if board[i][j] and board[i][j] != -1:
                q.append((i, j, board[i][j]))
    
    while q:
        row, col, density = q.popleft()
        spreaded_desity = density // 5
        
        cnt = 0
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                continue
            
            if board[next_row][next_col] == -1:
                continue
            
            board[next_row][next_col] += spreaded_desity
            cnt += 1
        
        board[row][col] -= spreaded_desity * cnt
        
def top_cycle(row, col, board):
    temp_row = row
    temp_col = col
    
    
    while True:
        if col == 0: break
        board[row][col] = board[row][col - 1]
        col -= 1
    
    
    while True:
        if row == 0: break
        board[row][col] = board[row - 1][col]
        row -= 1
        
    while True:
        if col == num_col - 1: break
        board[row][col] = board[row][col + 1]
        col += 1
    
    while True:
        if row == temp_row: break
        board[row][col] = board[row + 1][col]
        row += 1
    
    board[temp_row][temp_col] = 0
    while True:
        if col == temp_col: break
        board[row][col] = board[row][col - 1]
        col -= 1
        
    board[temp_row][temp_col] = -1
        
def bottom_cycle(row, col, board):
    temp_row = row
    temp_col = col
    
    
    while True:
        if col == 0: break
        board[row][col] = board[row][col - 1]
        col -= 1
    
    
    while True:
        if row == num_row - 1: break
        board[row][col] = board[row + 1][col]
        row += 1
        
    while True:
        if col == num_col - 1: break
        board[row][col] = board[row][col + 1]
        col += 1
    
    while True:
        if row == temp_row: break
        board[row][col] = board[row - 1][col]
        row -= 1
    
    board[temp_row][temp_col] = 0
    
    while True:
        if col == temp_col: break
        board[row][col] = board[row][col - 1]
        col -= 1
    
    board[temp_row][temp_col] = -1

def cycle(board, top, bottom):
    # top cycle
    row, col = top
    top_cycle(row, col, board)
    
    row, col = bottom
    bottom_cycle(row, col, board)
    
board = [list(map(int, input().split())) for i in range(num_row)]

air = []

for i in range(num_row):
    for j in range(num_col):
        if board[i][j] == -1:
            air += [(i, j)]
            
top, bottom = air

for i in range(time):
    spread(board)
    cycle(board, top, bottom)


res = 0

for i in range(num_row):
    for j in range(num_col):
        if board[i][j] and board[i][j] != -1:
            res += board[i][j]

print(res)