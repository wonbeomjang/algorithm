import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
apples = []
direction = 0
commands = []
snake = [(0, 0)]
board = [[0 for j in range(N)] for i in range(N)]
board[0][0] = 1

for _ in range(K):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 2
    
L = int(input())

for _ in range(L):
    duration, rotate = input().split()
    commands += [[int(duration), rotate]]


def print_map(t):
    global N
    global board
    
    print(f'time: {t}')
    for i in range(N):
        for j in range(N):
            print(board[i][j], end='')
        print()
    print()

def turn(rotate):
    global direction
    if rotate == 'L':
        direction = (direction + 3) % 4
    else:
        direction = (direction + 1) % 4
        
def collision(row, col):
    global N
    global board
    
    if not (0 <= row < N and 0 <= col < N):
        return True
    if board[row][col] == 1:
        return True
    return False

time = 0
while True:
#    print_map(time)
    if commands and commands[0][0] == time:
        turn(commands[0][1])
        commands.pop(0)
    
    time += 1
    
    row, col = snake[-1]
    next_row = row + dxdy[direction][0]
    next_col = col + dxdy[direction][1]
    
    if collision(next_row, next_col):
        break
    
    flag = board[next_row][next_col] == 0
    
    snake.append((next_row, next_col))
    board[next_row][next_col] = 1
    
    if flag:
        row, col = snake[0]
        board[row][col] = 0
        snake.pop(0)
        
print(time)