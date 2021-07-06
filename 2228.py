import sys

input = lambda: sys.stdin.readline().strip()

r1, c1, r2, c2 = map(int, input().split())
# r1, c1, r2, c2 = -3, -3, 0, 0
num_row = r2 - r1 + 1
num_col = c2 - c1 + 1

board = [[0] * num_col for i in range(num_row)]

def calc(row, col):
    area = max(abs(row), abs(col))
    # min_val: (2 * area) ** 2
    # max_val: (2 * area + 1) ** 2
    
    max_val = (2 * area + 1) ** 2
    distance = 2 * area
    
    if row == col == area:
        return max_val
    
    if row == area:
        val = max_val - (area - col)
        
    elif col == -area:
        val = max_val - distance
        val =     val - (area - row)
        
    elif row == -area:
        val = max_val - 2 * distance
        val =     val - (area + col)
    else:
        val = max_val - 3 * distance
        val =     val - (area + row)
    
    return val

n1 = len(str(calc(r1, c1)))
n2 = len(str(calc(r1, c2)))
n3 = len(str(calc(r2, c1)))
n4 = len(str(calc(r2, c2)))

just_len = max(n1, n2, n3, n4)

for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        val = str(calc(i, j))
        val_len = len(val)
        
        string = ' ' * (just_len - val_len) + val
        print(string, end=' ')
        
    print()