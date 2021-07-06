import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
num = int(input())

def calc(row, col):
    row -= (n + 1) // 2 - 1
    col -= (n + 1) // 2 - 1
    
    area = max(abs(row), abs(col))
    max_val = (2 * area + 1) ** 2
    distance = 2 * area
    
    if -row == -col == area:
        return max_val
    
    if col == -area:
        val = max_val - 0 * (distance)
        val = val - (area + row)
    elif row == area:
        val = max_val - 1 * (distance)
        val = val - (area + col)
    elif col == area:
        val = max_val - 2 * (distance)
        val = val - (area - row)
    else:
        val = max_val - 3 * (distance)
        val = val - (area - col)
    
    return val


for i in range(0, n):
    for j in range(0, n):
        val = calc(i, j)
        if val == num:
            ans = (i + 1, j + 1)
        print(f'{val}', end=' ')
    print()

print(*ans)
