import sys

input = lambda: sys.stdin.readable().strip()

n, k = map(int, input().split())

WHITE = 0
RED   = 1
BLUE  = 2

RIGHT = 1
LEFT  = 2
UP    = 3
DOWN  = 4

board  = [list(map(int, input().split())) for i in range(n)]
pieces = [[[] for i in range(n)] for j in range(n)]

for i in range(k):
    rwo, col, direction = map(int, input().split())
    pieces[row][col] += [(i, direction)]
