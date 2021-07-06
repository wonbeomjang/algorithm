import sys
from copy import deepcopy

input = lambda: sys.stdin.readline().strip()

num_row = num_col = int(input())

UP    = 0
DOWN  = 1
LEFT  = 2
RIGHT = 3

def shift(board, direction):
    # 상
    if direction == UP:
        for j in range(num_col):
            index = 0
            for i in range(num_row):
                if board[i][j]:
                    data = board[i][j]
                    board[i][j] = 0
                    
                    if not board[index][j]:
                        board[index][j] = data
                        
                    elif board[index][j] == data:
                        board[index][j] = 2 * data
                        index += 1
                    
                    else:
                        index += 1
                        board[index][j] = data
    
    # 하
    elif direction == DOWN:
        for j in range(num_col):
            index = num_row - 1
            for i in range(num_row - 1, -1, -1):
                if board[i][j]:
                    data = board[i][j]
                    board[i][j] = 0
                    
                    if not board[index][j]:
                        board[index][j] = data
                        
                    elif board[index][j] == data:
                        board[index][j] = 2 * data
                        index -= 1
                    
                    else:
                        index -= 1
                        board[index][j] = data
                        
    # 좌
    elif direction == LEFT:
        for i in range(num_row):
            index = 0
            for j in range(num_col):
                if board[i][j]:
                    data = board[i][j]
                    board[i][j] = 0
                    
                    if not board[i][index]:
                        board[i][index] = data
                    
                    elif board[i][index] == data:
                        board[i][index] = 2 * data
                        index += 1
                    
                    else:
                        index += 1
                        board[i][index] = data
    
    # 우 
    else:
        for i in range(num_row):
            index = num_col - 1
            for j in range(num_col - 1, -1, -1):
                if board[i][j]:
                    data = board[i][j]
                    board[i][j] = 0
                    
                    if not board[i][index]:
                        board[i][index] = data
                        
                    elif board[i][index] == data:
                        board[i][index] = 2 * data
                        index -= 1
                    
                    else:
                        index -= 1
                        board[i][index] = data
                    
                    
def print_board(board):
    for subline in board:
        print(' '.join(map(str, subline)))

def get_max_num(board):
    ans = 0
    for subline in board:
        ans = max(ans, *subline)
    return ans

ans = 0

def dfs(cnt, board):
    global ans
    if cnt == 5:
        return
    
    for direction in (UP, DOWN, RIGHT, LEFT):
        temp = deepcopy(board)
        shift(board, direction)
        ans = max(ans, get_max_num(board))
        
        dfs(cnt + 1, board)
        board = temp

board = [list(map(int, input().split())) for i in range(num_row)]
dfs(0, board)

print(ans)