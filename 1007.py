import math
import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())
ans = float('inf')



def dfs(cnt, index):
    global ans
    global N
    global is_end
    global points
    
    if cnt == N // 2:
        x, y = 0, 0
        
        for i in range(N):
            if is_end[i]:
                x += points[i][0]
                y += points[i][1]
            else:
                x -= points[i][0]
                y -= points[i][1]
        
        ans = min(ans, math.sqrt(x ** 2 + y ** 2))
        return 
        
    if index >= N:
        return
    
    dfs(cnt, index + 1)
    is_end[index] = True
    dfs(cnt + 1, index + 1)
    is_end[index] = False
          

for _ in range(T):
    N = int(input())
    is_end = [False for i in range(N)]
    points = []
    ans = float('inf')
    for _ in range(N):
        start, end = map(int, input().split())
        points += [[start, end]]
    
    dfs(0, 0)
    
    print(f'{ans:.12f}')