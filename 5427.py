import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))


num_tests = int(input())
num_col, num_row = 0, 0
board = []

def print_board():
    print('\n'.join([''.join(line) for line in board]))
    
    print()
    
def bfs():
    visited = [[0] * num_col for _ in range(num_row)]
    
    while s_q:
        flen = len(f_q)
        
        while flen:
            flen -= 1
            row, col = f_q.popleft()
            
            for dr, dc in drdc:
                next_row = row + dr
                next_col = col + dc
                
                if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                    continue
                
                if board[next_row][next_col] != '#' and board[next_row][next_col] != '*':
                    board[next_row][next_col] = '*'
                    f_q.append((next_row, next_col))
        
        slen = len(s_q)
        
        while slen:
            slen -= 1
            row, col = s_q.popleft()
            
            if row == 0 or col == 0 or row + 1 == num_row or col + 1 == num_col:
                return visited[row][col] + 1
            
            for dr, dc in drdc:
                next_row = row + dr
                next_col = col + dc
                
                if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                    continue
                
                if board[next_row][next_col] == '.' and not visited[next_row][next_col]:
                    s_q.append((next_row, next_col))
                    visited[next_row][next_col] = visited[row][col] + 1
                    board[next_row][next_col] = '@'
                    
        
    return 'IMPOSSIBLE'


for _ in range(num_tests):
    s_q = deque()
    f_q = deque()

    num_col, num_row = map(int, input().split())
    board = [list(input()) for _ in range(num_row)]
    
    for i in range(num_row):
        for j in range(num_col):
            if board[i][j] == '@':
                s_q.append((i, j))
            
            if board[i][j] == '*':
                f_q.append((i, j))
                
    print(bfs())

