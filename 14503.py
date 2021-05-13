NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

drdc = [[-1, 0], [0, 1], [1, 0], [0, -1]]

num_row, num_col = map(int, input().split())
row, col, dir = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(num_row)]
cnt = 0

def dfs(row, col, dir):
    global board, visited
    global cnt
    
    if not board[row][col]:
        board[row][col] = 2
        cnt += 1
    
    for i in range(4):
        dir = (dir + 3) % 4
        
        next_row = row + drdc[dir][0]
        next_col = col + drdc[dir][1]
        
        if not board[next_row][next_col]:
            dfs(next_row, next_col, dir)
            return
    
    next_row = row - drdc[dir][0]
    next_col = col - drdc[dir][1]
    
    if board[next_row][next_col] == 1:
        return
    else:
        dfs(next_row, next_col, dir)

dfs(row, col, dir)
print(cnt)