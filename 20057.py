import sys

input = lambda: sys.stdin.readline().strip()
drdc = ((0, -1), (1, 0), (0, 1), (-1, 0))

rate = []

rate.append([[0,0,2,0,0],[0,10,7,1,0],[5,0,0,0,0],[0,10,7,1,0],[0,0,2,0,0]])
rate.append([[0,0,0,0,0],[0,1,0,1,0],[2,7,0,7,2],[0,10,0,10,0],[0,0,5,0,0]])
rate.append([[0,0,2,0,0],[0,1,7,10,0],[0,0,0,0,5],[0,1,7,10,0],[0,0,2,0,0]])
rate.append([[0,0,5,0,0],[0,10,0,10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]])

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]

ans = 0

def wind(row, col, direction):
    global board, ans
    
    total_sand = board[row][col]
    remaind = total_sand
    board[row][col] = 0
    
    for i in range(5):
        for j in range(5):
            next_row = row + i - 2
            next_col = col + j - 2
            if rate[direction][i][j]:
                sand = int(total_sand / 100 * rate[direction][i][j])
                remaind -= sand
                
                if not (0 <= next_row < n and 0 <= next_col < n):
                    ans += sand
                else:
                    board[next_row][next_col] += sand
    
    next_row = row + drdc[direction][0]
    next_col = col + drdc[direction][1]
    
    if not (0 <= next_row < n and 0 <= next_col < n):
        ans += remaind
    else:
        board[next_row][next_col] += remaind
        
def print_board():
    for i in range(n):
        for j in range(n):
            print(f'{board[i][j]: 3}', end='')
        print()

row = col = n // 2
distance = 1
flag = True

while flag:
    for d in range(4):
        dr, dc = drdc[d]
        
        for i in range(distance):
            row += dr
            col += dc
            
            wind(row, col, d)
            
            if row == col == 0:
                flag = False
                break
        if not flag:
            break
        
        if d % 2:
            distance += 1
            
        
print(ans)