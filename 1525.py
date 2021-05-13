import sys
from collections import deque

input = sys.stdin.readline

drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))

target = '123456780'

board = ''
for _ in range(3):
     board += input().replace(' ', '').replace('\n', '')

def bfs(board):
    q = deque()
    visited = set()
    
    pos = board.find('0')
    visited.add(board)
    
    row = pos // 3
    col = pos % 3
    
    q.append((row, col, board, 0))
    while q:
        row, col, board, num_move = q.popleft()
        
        if board == target:
            return num_move
        
        pos = 3 * row + col
    
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
        
            if 0 <= next_row < 3 and 0 <= next_col < 3:
                
                next_pos = 3 * next_row + next_col
                next_board = list(board)
                next_board[next_pos], next_board[pos] = next_board[pos], next_board[next_pos]
                next_board = ''.join(next_board)
            
                if next_board not in visited:
                    q.append((next_row, next_col, next_board, num_move + 1))
                    visited.add(next_board)
    return -1
    
print(bfs(board))