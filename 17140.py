import sys
from collections import Counter

input = lambda: sys.stdin.readline().strip()

row, col, target = map(int, input().split())

row -= 1
col -= 1

arr = [list(map(int, input().split())) for i in range(3)]

def RC(arr):
    max_len = 0
    for i in range(len(arr)):
        counter = {}
        for j in range(len(arr[i])):
            if arr[i][j] not in counter:
                counter[arr[i][j]] = 1
            else:
                counter[arr[i][j]] += 1
                
        arr[i] = []
        for num, count in sorted(counter.items(), key=lambda x: (x[1], x[0])):
            arr[i] += [num, count]
        
        max_len = max(max_len, len(arr[i]))
    
    for i in range(len(arr)):
        if len(arr[i]) < max_len:
            arr[i] += [0] * (max_len - len(arr[i]))
        arr[i] = arr[i][:100]
    return arr

def print_arr(arr):
    print()
    for line in arr:
        for e in line:
            print(f'{e:3}', end='')
        print()

cnt = 0

while True:
    num_row = len(arr)
    num_col = len(arr[0])
    if cnt > 100:
        cnt = -1
        break
    
    if (row < num_row and col < num_col) and arr[row][col] == target:
        break
    
    cnt += 1
    if num_row >= num_col:
        arr = RC(arr)
    else:
        arr = list(map(list, zip(*arr)))
        arr = RC(arr)
        arr = list(map(list, zip(*arr)))

print(cnt)

"""

        for i, (num, count) in enumerate(sorted(counter.items(), key=lambda x: (x[1], x[0]))):
            if i > 100:
                break
"""
