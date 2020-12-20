from sys import stdin, stdout;

n = int(stdin.readline())
k = int(stdin.readline())

def getIndex(mid: int) -> int:
    global n
    cnt = 0
    
    for i in range(1, n + 1):
        cnt += min(n, mid // i)
        
    return cnt


left = 0
right = n * n

while left <= right:
    mid = (left + right) // 2
    if k <= getIndex(mid):
        right = mid - 1
    else:
        left = mid + 1
        
print(left)