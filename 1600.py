from collections import deque

drdc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
jump_drdx = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

def bfs():
    global board, drdc, jump_drdx
    q = deque()
    q.append((0, 0, 0, 0))
    visited[0][0][0] = True
    
    while q:
        cnt, knight, row, col = q.popleft()
        
        if row == num_row - 1 and col == num_col - 1:
            return cnt
        
        if knight < num_jump:
            for (dr, dc) in jump_drdx:
                next_row = row + dr
                next_col = col + dc 
                
                if (0 <= next_row < num_row) and (0 <= next_col < num_col):
                    if not visited[knight + 1][next_row][next_col] and not board[next_row][next_col]:
                        visited[knight + 1][next_row][next_col] = True
                        q.append((cnt + 1, knight + 1, next_row, next_col))
            
        for (dr, dc) in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if 0 <= next_row < num_row and 0 <= next_col < num_col:
                if not visited[knight][next_row][next_col] and not board[next_row][next_col]:
                    visited[knight][next_row][next_col] = True
                    q.append((cnt + 1, knight, next_row, next_col))
    return -1

num_jump = int(input())
num_col, num_row = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(num_row)]

visited = [[[False for i in range(num_col)] for i in range(num_row)] for i in range(num_jump + 1)]
print(bfs())