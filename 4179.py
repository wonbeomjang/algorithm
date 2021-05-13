import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

num_row, num_col = map(int, input().split())

board = [list(input()) for _ in range(num_row)]
drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))

j_q = deque()
f_q = deque()

for i in range(num_row):
    for j in range(num_col):
        if board[i][j] == 'J':
            j_q.append((i, j))
            
        if board[i][j] == 'F':
            f_q.append((i, j))

def print_board():
    print('\n'.join([''.join(line) for line in board]))
    
    print()
  
def bfs():
    j_visited = [[0] * num_col for _ in range(num_row)]
    
    
    while j_q:
        jlen = len(j_q)
        while jlen:
            jlen -= 1
            row, col = j_q.popleft()
            
            if (row == num_row - 1 or col == num_col - 1 or row == 0 or col == 0) and board[row][col] != 'F':
                return j_visited[row][col] + 1
            
            
            for dr, dc in drdc:
                next_row = row + dr
                next_col = col + dc
                
                if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                    continue
                
                if not j_visited[next_row][next_col] and board[next_row][next_col] == '.' and board[row][col] != 'F':
                    j_visited[next_row][next_col] = j_visited[row][col] + 1
                    board[next_row][next_col] = 'J'
                    j_q.append((next_row, next_col))
        
        if not j_q: break
    
        flen = len(f_q)
        
        while flen:
            flen -= 1
            row, col = f_q.popleft()
            
            for dr, dc in drdc:
                next_row = row + dr
                next_col = col + dc
                
                if not (0 <= next_row < num_row and 0 <= next_col < num_col):
                    continue
                
                if board[next_row][next_col] != '#' and board[next_row][next_col] != 'F':
                    board[next_row][next_col] = 'F'
                    f_q.append((next_row, next_col))
                
    return 'IMPOSSIBLE'
    
print(bfs())
    