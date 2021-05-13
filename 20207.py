import sys

input = lambda: sys.stdin.readline().strip()

num_schedules = int(input())

board = [0] * 366

schedules = []

for _ in range(num_schedules):
    start, end = map(int, input().split())
    
    for i in range(start, end + 1):
        board[i] += 1
    
width = 0
height = 0
res = 0

for i in range(366):
    if board[i]:
        width += 1
        height = max(height, board[i])
    else:
        res += width * height    
        width = 0
        height = 0
print(res)
        
    
