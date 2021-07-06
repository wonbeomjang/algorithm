import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

cnt = 0
q = deque()
MAX_NUM = 100001
visited = [0] * MAX_NUM

N, K = map(int, input().split())

q.append(N)
visited[N] = 1

while q:
    p = q.popleft()
    if p == K:
        cnt += 1
    
    for n_p in (p + 1, p - 1, p * 2):
        if 0 <= n_p < MAX_NUM:
            if not visited[n_p] or visited[n_p] == visited[p] + 1:
                q.append(n_p)
                visited[n_p] = visited[p] + 1
                
print(cnt)
print(visited[K] - 1)