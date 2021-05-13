import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

q = deque()

def bfs():
    max_num = -1
    visited = set()
    
    qlen = len(q)
    while qlen:
        qlen -= 1
        num = q.popleft()
        length = len(f'{num}')
        
        for (p1, p2) in combinations(range(length), 2):
            
            swaped_num = list(num)
            n1, n2 = swaped_num[p1], swaped_num[p2]
            swaped_num[p1], swaped_num[p2] = n2, n1
            
            if swaped_num[0] == '0':
                continue
            
            swaped_num = ''.join(swaped_num)
        
            if not swaped_num in visited:
                max_num = max(max_num, int(swaped_num))
                q.append(swaped_num)
                visited.add(swaped_num)
                
    
    return max_num
    
def solution(N, K):
    q.append(str(N))
    while K:
        ans = bfs()
        K -= 1
    
    print(ans)
    
solution(*map(int, input().split()))