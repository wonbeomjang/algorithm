import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

num_ladder, num_snakes = map(int, input().split())
ladders = {}
snakes = {}

for i in range(num_ladder):
    s, t = map(int, input().split())
    ladders[s] = t

for i in range(num_snakes):
    s, t = map(int, input().split())
    snakes[s] = t

q = deque([1])
visited = [200] * 101
visited[1] = 0

while q:
    pos = q.popleft()

    for i in range(6, 0, -1):
        next_pos = pos + i
        if next_pos > 100:
            continue

        if next_pos in ladders:
            next_pos = ladders[next_pos]
        elif next_pos in snakes:
            next_pos = snakes[next_pos]

        if visited[pos] + 1 < visited[next_pos]:
            visited[next_pos] = visited[pos] + 1
            q.append(next_pos)

print(visited[100])

