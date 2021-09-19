import sys
from itertools import chain

input = lambda: sys.stdin.readline().strip()
drdc = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
cross = ((1, 1), (1, -1), (-1, 1), (-1, -1))

n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
cloud = set([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])

commands = []
for i in range(m):
    dir, dis = map(int, input().split())
    commands += [(dir - 1, dis)]

def print_board():
    print()
    for i in range(n):
        for j in range(n):
            print(f'{board[i][j]:3}', end='')
        print()

def move_and_rain(dir, dis):
    global cloud
    temp = set()
    
    for row, col in cloud:
        for _ in range(dis):
            row = (row + drdc[dir][0]) % n
            col = (col + drdc[dir][1]) % n
            
        temp.add((row, col))
        board[row][col] += 1
    
    cloud = temp
    
def copy():
    global cloud, board
    
    for row, col in cloud:
        cnt = 0
        for dr, dc in cross:
            next_row = row + dr
            next_col = col + dc
            
            if 0 <= next_row < n and 0 <= next_col < n and board[next_row][next_col]:
                cnt += 1
        
        board[row][col] += cnt 

def make_cloud():
    global cloud
    temp = set()
    for i in range(n):
        for j in range(n):
            if board[i][j] > 1 and not (i, j) in cloud:
                board[i][j] -= 2
                temp.add((i, j))
    cloud = temp

for dir, dis in commands:
    move_and_rain(dir, dis)
    copy()
    make_cloud()

print(sum(chain(*board)))