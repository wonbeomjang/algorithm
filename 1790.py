import sys

input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())

num = ''
for i in range(1, n + 1):
    length = len(f'{i}')
    
    if 0 <= k <= length:
        print(f'{i}'[k - 1])
        break
    
    k -= length
else:
    print(-1)