from collections import deque
import copy
import sys

sys.setrecursionlimit(1000000000)

drdc = [[0, 1], [0, -1], [1, 0], [-1, 0]]

num_row, num_col = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(num_row)]
prev_board = copy.deepcopy(board)

def melt():
    global num_row, num_col
    global board
    
    visited = [[False] * num_col for _ in range(num_row)]
    q = deque()
    q.append([0, 0])
    
    visited[0][0] = True
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                continue
            
            if not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                
                if board[next_row][next_col] == 1:
                    board[next_row][next_col] = 0
                else:
                    q.append([next_row, next_col])
                
            
    

def bfs(row, col, visited):
    global num_row, num_col
    global prev_board
    
    q = deque()
    q.append([row, col])
    
    visited[row][col] = True
    cnt = 1
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                continue
            
            if not visited[next_row][next_col] and prev_board[next_row][next_col]:
                q.append([next_row, next_col])
                visited[next_row][next_col] = True
                cnt += 1
                
    return cnt
                

def is_cheeze():
    global num_row, num_col
    global board
    
    for i in range(num_row):
        for j in range(num_col):
            if board[i][j] == 1:
                return True
                
    return False

def print_board():
    global prev_board
    
    for _ in range(num_col):
        print('___', end='')
    print()
    for sb in prev_board:
        for b in sb:
            print(b, end=' ')
        print()

time = 0

while True:
    if not is_cheeze():
        visited = [[False] * num_col for _ in range(num_row)]
        
        cnt = 0
        for i in range(num_row):
            for j in range(num_col):
                if prev_board[i][j] and not visited[i][j]:
                    res = bfs(i, j, visited)
                    cnt += res
        
        print(time)
        print(cnt)
        
        break
    
    visited = [[False] * num_col for _ in range(num_row)]
    prev_board = copy.deepcopy(board)
    melt()
    time += 1