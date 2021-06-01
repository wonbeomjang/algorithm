import sys

input = lambda: sys.stdin.readline().strip()

set_length = int(input())
set_num = sorted(map(int, input().split()))
set_num = [0] + set_num

n = int(input())

res = 0

left = 0
right = 0

if n in set_num:
    print(0)
    sys.exit()
    
for num in set_num:
    if num < n:
        left = num + 1
    else:
        right = num - 1
        break

print(right - left + (n - left) * (right - n))

3 + 1 * 2