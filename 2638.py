import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))

num_row, num_col = map(int, input().split())

def get_melt_block(board):
    global num_row, num_col
    
    q = deque()
    res = deque()
    
    visited = [[0] * num_col for i in range(num_row)]
    visited_cheeze = set()
    
    q.append((0, 0))
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                continue
            
            if not visited[next_row][next_col]:
                if board[next_row][next_col]:
                    if (next_row, next_col) in visited_cheeze:
                        visited[next_row][next_col] = True
                        res.append((next_row, next_col))
                        
                    else:
                        visited_cheeze.add((next_row, next_col))
                else:
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col))
    
    return res

def melt(board, blocks: deque):
    while blocks:
        row, col = blocks.popleft()
        board[row][col] = 0
        

def print_board(board):
    for subline in board:
        print(' '.join(map(str, subline)))

board = [list(map(int, input().split())) for i in range(num_row)]

cnt = 0
while True:
    block = get_melt_block(board)
    if not block:
        break
    
    cnt += 1
    melt(board, block)
print(cnt)