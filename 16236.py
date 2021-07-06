import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
drdc = ((-1, 0), (0, -1), (0, 1), (1, 0))

num_row = num_col = int(input())

def get_shark_info(board):
    for i in range(num_row):
        for j in range(num_col):
            if board[i][j] == 9:
                row, col, size = i, j, 2
    
    board[row][col] = 0
    return row, col, size

def bfs(board, row, col, size):
    q = deque()
    visited = [[False] * num_col for i in range(num_row)]
    
    eat = []
    
    q.append((row, col, 0))
    visited[row][col] = True
    
    while q:
        row, col, time = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                continue
            
            if not visited[next_row][next_col] and board[next_row][next_col] <= size:
                if 0 < board[next_row][next_col] < size:
                    eat += [(time + 1, next_row, next_col)]
                
                visited[next_row][next_col] = True
                q.append((next_row, next_col, time + 1))
    if eat:
        eat.sort()
        time, row, col = eat[0]
        board[row][col] = 0
        return row, col, time
    else:
        return -1, -1, -1

def print_board(board):
    print()
    for sub in board:
        print(' '.join(map(str, sub)))

board = [list(map(int, input().split())) for i in range(num_row)]
row, col, size = get_shark_info(board)

cnt = 0
time = 0

while True:
    row, col, spend_time = bfs(board, row, col, size)
    if spend_time == -1:
        break
    time += spend_time
    cnt += 1
    
    if cnt == size:
        cnt = 0
        size += 1
    
    # print_board(board)
    # print(row, col, size)
print(time)