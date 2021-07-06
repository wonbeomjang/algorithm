import sys

input = lambda: sys.stdin.readline().strip()

arr = [input() for i in range(36)]
arr += [arr[0]]

if len(set(arr)) != 36:
    print('Invalid')
    sys.exit(0)
    
for i in range(36):
    row, col = int(arr[i][1]), ord(arr[i][0])
    next_row, next_col = int(arr[i + 1][1]), ord(arr[i + 1][0])
    
    if abs(next_row - row) * abs(next_col - col) != 2:
        print('Invalid')
        sys.exit(0)
        


print('Valid')