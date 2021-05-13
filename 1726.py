from collections import deque
import sys

input = sys.stdin.readline

EAST = 1
WEST = 2
SOUTH = 3
NORTH = 0

drdc = [[-1, 0], [0, 1], [0, -1], [1, 0]]

num_row, num_col = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(num_row)]

start_row, start_col, start_dir = map(int, input().split())
end_row, end_col, end_dir = map(int, input().split())

start_row, start_col, start_dir = start_row - 1, start_col - 1, start_dir % 4
end_row, end_col, end_dir = end_row - 1, end_col - 1, end_dir % 4

visited = [[[0] * num_col for _ in range(num_row)] for _ in range(4)]
    
q = deque()

def turn_right(row, col, dir):
    global q
    
    if dir == NORTH: next_dir = EAST
    elif dir == EAST: next_dir = SOUTH
    elif dir == SOUTH: next_dir = WEST
    else: next_dir = NORTH
    
    if not visited[next_dir][row][col]:
        q.append([row, col, next_dir])
        visited[next_dir][row][col] = visited[dir][row][col] + 1
    
def turn_left(row, col, dir):
    global q
    
    if dir == NORTH: next_dir = WEST
    elif dir == WEST: next_dir = SOUTH
    elif dir == SOUTH: next_dir = EAST
    else: next_dir = NORTH
    
    if not visited[next_dir][row][col]:
        q.append([row, col, next_dir])
        visited[next_dir][row][col] = visited[dir][row][col] + 1
    
def move(row, col, dir):
    global q
    global visited
    global board
    
    next_row = row
    next_col = col
    
    for dis in range(1, 4):
        next_row += drdc[dir][0]
        next_col += drdc[dir][1]
        
        if not (0 <= next_row < num_row and 0 <= next_col < num_col) or board[next_row][next_col]:
            return
        
        if not visited[dir][next_row][next_col]:
            q.append([next_row, next_col, dir])
            visited[dir][next_row][next_col] = visited[dir][row][col] + 1
            

def bfs(row, col, dir):
    global num_row, num_col
    global end_row, end_col, end_dir
    global board
    global visited
    global q

    
    visited[dir][row][col] = 1
    q.append([row, col, dir])
    
    while q:
        row, col, dir = q.popleft()
        
        if row == end_row and col == end_col and dir == end_dir:
            return visited[dir][row][col] - 1
            
        turn_right(row, col, dir)
        turn_left(row, col, dir)
        move(row, col, dir)
        
        
    
print(bfs(start_row, start_col, start_dir))
