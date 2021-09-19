import sys
from itertools import chain
from copy import deepcopy

input = lambda: sys.stdin.readline().strip()
green_board = [[0 for i in range(4)] for i in range(10)]
blue_board = [[0 for i in range(4)] for i in range(10)]

def drop_block(board, block):
    r1, c1 = block[0]
    r2, c2 = block[-1]
    next_r1 = r1
    next_r2 = r2
    for i in range(10):
        next_r1 = r1 + i
        next_r2 = r2 + i
        
        if next_r1 == 9 or next_r2 == 9 or board[next_r1 + 1][c1] or board[next_r2 + 1][c2]:
            break
    
    
    board[next_r1][c1] = 1
    board[next_r2][c2] = 1
    
    return board

def delete_block(board):
    score = 0
    for i in range(9, 3, -1):
        if sum(board[i]) == 4:
            score += 1
            for j in range(i, 2, -1):
                board[j] = deepcopy(board[j - 1])
                
    return score

def delete_special(board):
    cnt = 0
    if sum(board[4]) > 0: cnt += 1
    if sum(board[5]) > 0: cnt += 1
    
    for i in range(9, 3, -1):
        board[i] = deepcopy(board[i - cnt])

def print_board(board):
    print()
    for i in range(10):
        for j in range(4):
            print(f'{board[i][j]:3d}', end='')
        print()

n = int(input())
score = 0

for i in range(n):
    block_type, row, col = map(int, input().split())
    if block_type == 1: block = [(row, col)]
    elif block_type == 2: block = [(row, col), (row, col + 1)]
    elif block_type == 3: block = [(row, col), (row + 1, col)]
    
    drop_block(green_board, block)
    drop_block(blue_board, [tuple(reversed(b)) for b in block])
    
    
    score += delete_block(green_board)
    score += delete_block(blue_board)
    
    delete_special(green_board)
    delete_special(blue_board)
    

print(score)
print(sum(chain(*blue_board)) + sum(chain(*green_board)))