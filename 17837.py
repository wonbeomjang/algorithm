import sys

input = lambda: sys.stdin.readline().strip()

drdc = ((0, 1), (0, -1), (-1, 0), (1, 0))
WHITE = 0
RED   = 1
BLUE  = 2

n, k = map(int, input().split())
color = [list(map(int, input().split())) for i in range(n)]
board = [[[] for i in range(n)] for i in range(n)]

pieces = [0] * k

for i in range(k):
    row, col, dir = map(int, input().split())
    pieces[i] = (row - 1, col - 1, len(board[row - 1][col - 1]), dir - 1)
    board[row - 1][col - 1] += [i]
    

def play():
    i = 0
    
    while i < k:
        row, col, index, dir = pieces[i]
        
        next_row = row + drdc[dir][0]
        next_col = col + drdc[dir][1]
        
        if not (0 <= next_row < n and 0 <= next_col < n) or color[next_row][next_col] == BLUE:
            dir += -1 if dir % 2 else 1
            
            next_row = row + drdc[dir][0]
            next_col = col + drdc[dir][1]

            pieces[i] = (row, col, index, dir)
            
            if not (0 <= next_row < n and 0 <= next_col < n) or color[next_row][next_col] == BLUE:
                pass
            else:
                continue
            
            
            
        elif color[next_row][next_col] == WHITE:
            for idx, j in enumerate(board[row][col][index:]):
                pieces[j] = (next_row, next_col, len(board[next_row][next_col]) + idx, pieces[j][3])
                
            board[next_row][next_col] += board[row][col][index:]
            del board[row][col][index:]
            
        elif color[next_row][next_col] == RED:
            for idx, j in enumerate(board[row][col][index:]):
                pieces[j] = (next_row, next_col, len(board[next_row][next_col]) + len(board[row][col][index:]) - idx - 1, pieces[j][3])
            
            board[next_row][next_col] += reversed(board[row][col][index:])
            del board[row][col][index:]
            
        i += 1
        
        for i1 in range(n):
            for j1 in range(n):
                if len(board[i1][j1]) >= 4:
                    return False
            
    return True

cnt = 0

while play():
    cnt += 1
    if cnt >= 1000:
        cnt = -2
        break
print(cnt + 1)