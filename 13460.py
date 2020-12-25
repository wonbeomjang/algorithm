from collections import deque

num_row, num_col = map(int, input().split())

dxdy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
visited = [[[[False for j in range(10)] for i in range(10)] for _ in range(10)] for _ in range(10)]
    

def tilt(x, y, d):
    for i in range(10):
        x += dxdy[d][0]
        y += dxdy[d][1]
        
        if board[y][x] == 'O':
            return x, y
        if board[y][x] == '#':
            x -= dxdy[d][0]
            y -= dxdy[d][1]
            return x, y
                    
board = []
for i in range(num_row):
    board += [list(input())]
    
    for j in range(num_col):
        if board[i][j] == 'B':
            by, bx = i, j
            board[i][j] = '.'
        if board[i][j] == 'R':
            ry, rx = i, j
            board[i][j] = '.'
        if board[i][j] == 'O':
            hy, hx = i, j
            
q = deque()
q.append([0, rx, ry, bx, by])    
visited[rx][ry][bx][by] = True

def bfs():
    
    while q:
        cur = q.popleft()
        
        depth, rx, ry, bx, by = cur
        if rx == hx and ry == hy:
            return depth
                
        if cur[0] > 10:
            return -1
        
        for i in range(4):
            # 상 하 좌 우
            depth, rx, ry, bx, by = cur
            
            rx, ry = tilt(rx, ry, i)
            bx, by = tilt(bx, by, i)
            
            if bx == hx and by == hy:
                continue
            
            if rx == bx and ry == by:
                if i == 0 :
                    ry, by = (ry + 1, by) if cur[2] > cur[4] else (ry, by + 1)
                elif i == 1:
                    ry, by = (ry, by - 1) if cur[2] > cur[4] else (ry - 1, by)
                elif i == 2:
                    rx, bx = (rx + 1, bx) if cur[1] > cur[3] else (rx, bx + 1)
                else:
                    rx, bx = (rx, bx - 1) if cur[1] > cur[3] else (rx - 1, bx)
                    
            
            if not visited[rx][ry][bx][by]:
                q.append([depth + 1, rx, ry, bx, by])
                visited[rx][ry][bx][by] = True
                
    return -1
def print_map(board):
    for i in range(num_row):
        for j in range(num_col):
            print(board[i][j], end=' ')
        print()

print(bfs())