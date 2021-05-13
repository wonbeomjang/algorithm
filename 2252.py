import sys
from collections import deque

input = sys.stdin.readline

num_people, num_compare = map(int, input().split())

edges = [[] for _ in range(num_people + 1)]
indegree = [0 for _ in range(num_people + 1)]

for _ in range(num_compare):
    front, back = map(int, input().split())
    edges[front].append(back)
    indegree[back] += 1

q = deque()

for i in range(1, num_people + 1):
    if not indegree[i]:
        q.append(i)

res = []

while q:
    v = q.popleft()
    print(v, end=' ')
    
    for nv in edges[v]:
        indegree[nv] -= 1
        if not indegree[nv]:
            q.append(nv)

print('@'.join(map(str, res)))