import sys
from collections import deque

input = sys.stdin.readline

num_people = int(input())

edge = [[] for _ in range(num_people + 1)]

def bfs(p: int):
    global num_people
    
    visited = [False for _ in range(num_people + 1)]
    visited[0] = True
    visited[p] = True
    
    q = deque()
    q.append([p, 1])
    
    while q:
        p, dis = q.popleft()
        
        for n_p in edge[p]:
            if not visited[n_p]:
                visited[n_p] = True
                q.append([n_p, dis + 1])
                
        if all(visited):
            return dis
    

while True:
    p1, p2 = map(int, input().split())
    
    if p1 == -1 and p2 == -1:
        break
    
    edge[p1] += [p2]
    edge[p2] += [p1]
    
min_score = float('inf')
candidate = []

for i in range(1, num_people + 1):
    res = bfs(i)
    
    if res < min_score:
        min_score = res
        candidate = [i]
        
    elif res == min_score:
        candidate += [i]
        
print(f'{min_score} {len(candidate)}')
print(f' '.join(map(str, sorted(candidate))))
