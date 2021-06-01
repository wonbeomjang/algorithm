import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

num_people = int(input())

graph = [list(input()) for i in range(num_people)]

def bfs(start):
    q = deque()
    visited = [False] * num_people
    
    visited[start] = True
    q.append((start, 0))
    num_friends = 0
    
    while q:
        p, depth = q.popleft()
        
        if depth == 2:
            continue
        
        for i in range(num_people):
            if not visited[i] and graph[p][i] == 'Y':
                num_friends += 1
                q.append((i, depth + 1))
                visited[i] = True
                
    return num_friends

max_friends = 0

for i in range(num_people):
    max_friends = max(max_friends, bfs(i))
    
print(max_friends)