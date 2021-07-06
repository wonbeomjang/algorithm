import sys
from copy import deepcopy
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()
drdc = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

n, m, k = map(int, input().split())


def spring_summer(board, trees):
    for i in range(n):
        for j in range(n):
            len_tree = len(trees[i][j])
            for k in range(len_tree):
                if board[i][j] >= trees[i][j][k]:
                    board[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for _ in range(k, len_tree):
                        board[i][j] += trees[i][j].pop() // 2
                    break
            
def autumn_winter(board, trees, fertilize):
    for i in range(n):
        for j in range(n):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for dr, dc in drdc:
                        ni = i + dr
                        nj = j + dc
                
                        if not (0 <= ni < n and 0 <= nj < n):
                            continue
                        
                        trees[ni][nj] = [1] + trees[ni][nj]
            board[i][j] += fertilize[i][j] 
            
    
def print_board(board):
    print()
    for line in board:
        print(' '.join(map(str, line)))

board = [[5] * n for i in range(n)]
fertilize = [list(map(int, input().split())) for i in range(n)]

trees = [[[] for _ in range(n)] for i in range(n)]

for i in range(m):
    row, col, age = map(int, input().split())
    trees[row - 1][col - 1] += [age]

for i in range(k):
    spring_summer(board, trees)
    autumn_winter(board, trees, fertilize)

cnt = 0

for i in range(n):
    for j in range(n):
        if trees[i][j]:
            cnt += len(trees[i][j])

print(cnt)