import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = lambda: sys.stdin.readline().strip()

a, b, c = map(int, input().split())

def bfs(a, b, c):
    q = deque()
    visited = set()
    
    q.append((a, b, c))
    visited.add((a, b, c))
    
    while q:
        temp_num = q.popleft()
        
        if temp_num[0] == temp_num[1] == temp_num[2]:
            return 1
        
        for x, y in combinations(range(3), 2):
            nums = deepcopy(temp_num)
            nums = list(nums)
            if nums[x] == nums[y]:
                continue
            
            if nums[x] < nums[y]:
                nums[y] -= nums[x]
                nums[x] *= 2
            else:
                nums[x] -= nums[y]
                nums[y] *= 2
            
            nums = tuple(nums)
            
            if not nums in visited:
                q.append(nums)
                visited.add(nums)
                
            
    return 0
    
print(bfs(a, b, c))