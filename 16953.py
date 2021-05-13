import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

start_num, target_num = map(int, input().split())

def bfs():
    q = deque()
    visited = set()
    q.append((start_num, 0))
    
    while q:
        num, num_changed = q.popleft()
        if num == target_num:
            return num_changed + 1
            
        next_num_1 = num * 2
        next_num_2 = num * 10 + 1
        
        if not next_num_1 in visited and next_num_1 <= 10 ** 9:
            q.append((next_num_1, num_changed + 1))
            visited.add(next_num_1)
        if not next_num_2 in visited and next_num_2 <= 10 ** 9:
            q.append((next_num_2, num_changed + 1))
            visited.add(next_num_2)
            
    return -1
    
print(bfs())