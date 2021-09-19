import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

# up, down, left, right
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

UP    = 0
DOWN  = 1
LEFT  = 2
RIGHT = 3

num_row, num_col = map(int, input().split())
board = [list(input()) for i in range(num_row)]

for i in range(num_row):
    for j in range(num_col):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'O':
            hole = (i, j)

def tilt(ball, direction):
    row, col = ball
    
    for i in range(10):
        row += dr[direction]
        col += dc[direction]
        
        if board[row][col] == '#':
            row -= dr[direction]
            col -= dc[direction]
            
            return (row, col)
            
        if board[row][col] == 'O':
            return (row, col)
        
            
def bfs(red, blue, hole):
    q = deque()
    visited = set()
    
    q.append((red, blue, 0))
    visited.add((red, blue))
    
    while q:
        red, blue, cnt = q.popleft()
        
        if red == hole:
            return 1
            
        if cnt > 10:
            return 0
            
        temp_red = red
        temp_blue = blue
        
        for direction in range(4):
            
            red = tilt(temp_red, direction)
            blue = tilt(temp_blue, direction)
            
            if blue == hole:
                continue
            
            if red == blue:
                if direction == UP:
                    if temp_red[0] > temp_blue[0]: red = (red[0] + 1, red[1])
                    else: blue = (blue[0] + 1, red[1])
                
                elif direction == DOWN:
                    if temp_red[0] > temp_blue[0]: blue = (blue[0] - 1, blue[1])
                    else: red = (red[0] - 1, red[1])
                
                
                elif direction == LEFT:
                    if temp_red[1] > temp_blue[1]: red = (red[0], red[1] + 1)
                    else: blue = (blue[0], red[1] + 1)
                    
                else:
                    if temp_red[1] > temp_blue[1]: blue = (blue[0], blue[1] - 1)
                    else: red = (red[0], red[1] - 1)
            
            if not (red, blue) in visited:
                visited.add((red, blue))
                q.append((red, blue, cnt + 1))
    
    return 0


print(bfs(red, blue, hole))