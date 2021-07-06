import sys

input = lambda: sys.stdin.readline().strip()
drdc = ((-1, 0), (0, -1))
num_row, num_col = map(int, input().split())
num_construction = int(input())

dp = {}

construction = set()

for i in range(num_construction):
    row1, col1, row2, col2 = map(int, input().split())
    construction.add(tuple(sorted([(row1, col1), (row2, col2)])))
    
def dfs(row, col):
    # if (row, col) in dp:
    #     return dp[(row, col)]
        
    if row < 0 or col < 0:
        return 0
        
    if row == 0 and col == 0:
        dp[(0, 0)] = 1
        return dp[(row, col)]
        
    
    for dr, dc in drdc:
        next_row = row + dr
        next_col = col + dc 
        
        temp = tuple(sorted([(row, col), (next_row, next_col)]))
        dp[(row, col)] = 0
        
        if not temp in construction:
            # print(temp)
            dp[(row, col)] += dfs(next_row, next_col)
    
    return dp[(row, col)]

dfs(num_row, num_col)

for i in range(num_row):
    for j in range(num_col):
        print(f'{dp[(i, j)]:3}', end='')
    print()