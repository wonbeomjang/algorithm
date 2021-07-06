import sys

input = lambda: sys.stdin.readline().strip()

drdc = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
board = [[() for i in range(4)] for j in range(4)]
fish = {}
shark = (0, 0, 0)

for i in range(4):
    n1, d1, n2, d2, n3, d3, n4, d4 = map(int, input().split())
    board[i][0] = (n1, d1 - 1)
    board[i][1] = (n2, d2 - 1)
    board[i][2] = (n3, d3 - 1)
    board[i][3] = (n4, d4 - 1)
    
    fish[n1] = (i, 0, d1 - 1)
    fish[n2] = (i, 1, d2 - 1)
    fish[n3] = (i, 2, d3 - 1)
    fish[n4] = (i, 3, d4 - 1)

def eat(board, row, col):
    num, direction = board[row][col]
    del fish[num]
    board[row][col] = (-1, -1)
    return (row, col, direction)
    

def move(board, fish):
    for i in range(1, 17):
        if i in fish:
            row, col, direction = fish[i]
            
            while True:
                next_row = row + drdc[direction][0]
                next_col = col + drdc[direction][1]
                
                if not (0 <= next_row < 4 and 0 <= next_col < 4) or board[next_row][next_col] == (-1, -1):
                    direction = (direction + 1) % 8
                    continue
                
                if board[next_row][next_col] != (-1, -1):
                    next_num, next_direction = board[next_row][next_col]
                    
                    fish[i] = (next_row, next_col, direction)
                    fish[next_num] = (row, col, next_direction)
                    
                    board[row][col] = board[next_row][next_col]
                    board[next_row][next_col] = (i, direction)
                    
                else:
                    fish[i] = (next_row, next_col, direction)
                    board[row][col] = (-1, -1)
                    board[next_row][next_col] = (i, direction)
                    
                break
            
            print(i)
            print_board(board)

def print_board(board):
    print()
    for line in board:
        for n, d in line:
            print(f'{str((n, d)):10}', end='')
        print()

eat(board, 0, 0)
print_board(board)

move(board, fish)
print_board(board)