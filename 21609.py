import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
drdc = ((1, 0), (-1, 0), (0, 1), (0, -1))

n, num_color = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]

def print_board():
    global board
    print()
    for i in range(n):
        for j in range(n):
            print(f'{board[i][j]:3}', end='')
        print()

def bfs(row, col, visited):
    global board
    q = deque()
    color = board[row][col]
    cnt = 1
    num_rainbow = 0
    
    blocks = [(row, col)]
    rainbow_blocks = []
    
    q.append((row, col))
    visited[row][col] = True

    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < n and 0 <= next_col < n):
                continue
            
            if not visited[next_row][next_col]:
                if not board[next_row][next_col] or color == board[next_row][next_col]:
                    if not board[next_row][next_col]:
                        num_rainbow += 1
                        rainbow_blocks += [(next_row, next_col)]
                    
                    blocks += [(next_row, next_col)]
                    cnt += 1
                    q.append((next_row, next_col))
                    visited[next_row][next_col] = True
    
    for row, col in rainbow_blocks:
        visited[row][col] = 0

    return cnt, num_rainbow, blocks

def find_biggest_group():
    global board
    max_cnt = 0
    max_rainbow = 0
    visited = [[False] * n for i in range(n)]
    res = []
    
    for i in range(n):
        for j in range(n):
            if 0 < board[i][j] <= num_color and not visited[i][j]:
                cnt, num_rainbow, blocks = bfs(i, j, visited)
                if cnt < 2:
                    continue
                
                res += [(cnt, num_rainbow, i, j)]
    
    if not res:
        return res
    
    res.sort()
    _, _, row, col = res[-1]
    
    visited = [[False] * n for i in range(n)]
    _, _, blocks = bfs(row, col, visited)
    
    return blocks
    
def delete_group(group):
    global board
    
    cnt = len(group)
    
    for row, col in group:
        board[row][col] = -2
        
    return cnt * cnt
        
def fall():
    global board
    for j in range(n):
        for i in range(n - 2, -1, -1):
            if 0 <= board[i][j] <= num_color:
                for k in range(i, n - 1):
                    if board[k + 1][j] != -2:
                        break
                    board[k + 1][j] = board[k][j]
                    board[k][j] = -2

def rotate():
    global board
    board = list(map(list, zip(*board)))[::-1]
    
def play():
    group = find_biggest_group()
    if not group:
        return 0
        
    score = delete_group(group)
    fall()
    rotate()
    fall()
    
    return score

total_score = 0
while True:
    score = play()
    if not score: break
    total_score += score

print(total_score)