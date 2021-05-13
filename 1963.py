import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

prime_numbers = set()

for n in range(1000, 10000):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            break
    else:
        prime_numbers.add(f'{n}')
        

num_tests = int(input())

def bfs(start_num, target_num):
    q = deque()
    q.append((start_num, 0))
    visited = set()
    
    visited.add(start_num)
    
    while q:
        cur_num, num_changed = q.popleft()
        
        if cur_num == target_num:
            return num_changed
        
        
        for i in range(4):
            for n in range(10):
                if i == 0 and n == 0:
                    continue
                
                next_num = list(cur_num)
                next_num[i] = f'{n}'
                next_num = ''.join(next_num)
                
                if cur_num == next_num:
                    continue
                
                if (not next_num in visited) and (next_num in prime_numbers):
                    q.append((next_num, num_changed + 1))
                    visited.add(cur_num)
                
    return 'Impossible'        
                
        
for _ in range(num_tests):
    n1, n2 = input().split()
    print(bfs(n1, n2))