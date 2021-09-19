import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()
drdc = ((-1, 0), (0, 1), (0, -1), (1, 0))

n = int(input())
board = [[0] * n for i in range(n)]

peoples = []
adj = {}

like_dict = defaultdict(set)

for i in range(n * n):
    temp = list(map(int, input().split()))
    peoples += [(temp[0], set(temp[1:]))]
    like_dict[temp[0]] = set(temp[1:])
    
def set_seat(p, adj):
    global board
    max_zeros = -1
    max_like_p = -1
    i = j = 0
    
    pq = []
    
    for row in range(n):
        for col in range(n):
            num_zeros = 0
            num_like_p = 0
            for dr, dc in drdc:
                next_row = row + dr
                next_col = col + dc
                
                if not (0 <= next_row < n and 0 <= next_col < n):
                    continue
                
                if not board[next_row][next_col]:
                    num_zeros += 1
                elif board[next_row][next_col] in adj:
                    num_like_p += 1
            
            if not board[row][col] and (num_like_p > max_like_p or (num_like_p == max_like_p and num_zeros > max_zeros)):
                i = row
                j = col
                max_like_p = num_like_p
                max_zeros = num_zeros
                
    return i, j

def print_board():
    print()
    for line in board:
        print(' '.join(map(str, line)))

likes = 0
for p, a in peoples:
    row, col = set_seat(p, a)
    board[row][col] = p

for row in range(n):
    for col in range(n):
        num_like_p = 0
        
        like = like_dict[board[row][col]]
        
        for dr, dc in drdc:
            next_row = row + dr
            next_col = col + dc
            
            if not (0 <= next_row < n and 0 <= next_col < n):
                continue
            
            if board[next_row][next_col] in like:
                    num_like_p += 1
        
        if num_like_p:
            likes += 10 ** (num_like_p - 1)

print(likes)