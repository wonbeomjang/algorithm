import sys

input = lambda: sys.stdin.readline().strip()
drdc = ((-1, 0), (1, 0), (0, 1), (0, -1))

UP    = 0
DOWN  = 1
RIGHT = 2
LEFT  = 3

num_row, num_col, num_sharks = map(int, input().split())
board = [[[] for i in range(num_col)] for i in range(num_row)]

def catch(board, col):
    for i in range(num_row):
        if board[i][col]:
            size = board[i][col][2]
            board[i][col] = 0
            return size
            
    return 0

def move(board):
    temp = [[[] for i in range(num_col)] for i in range(num_row)]
    for i in range(num_row):
        for j in range(num_col):
            if board[i][j]:
                row, col, (speed, direction, size) = i, j, board[i][j]
                for _ in range(speed):
                    row += drdc[direction][0]
                    col += drdc[direction][1]
                    
                    
                    if not (0 <= row < num_row and 0 <= col < num_col):
                        row -= 2 * drdc[direction][0]
                        col -= 2 * drdc[direction][1]
                        
                        if direction % 2 == 1:
                            direction -= 1
                        else:
                            direction += 1
                            
                
                if not temp[row][col] or temp[row][col][2] <= size:
                    temp[row][col] = [speed, direction, size]
                    
    return temp
    
def print_board(baord):
    print()
    for line in board:
        for element in line:
            if element:
                print(element[2], end=' ')
            else:
                print(0, end=' ')
        print()

# row, col, speed, direction, size
for i in range(num_sharks):
    row, col, speed, direction, size = map(int, input().split())
    board[row - 1][col - 1] = [speed, direction - 1, size]

total = 0
for i in range(num_col):
    total += catch(board, i)
    board = move(board)

print(total)
