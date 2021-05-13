import heapq
import sys

input = sys.stdin.readline
N, K = map(int, input().split())

jams = [list(map(int, input().split())) for _ in range(N)]
knapsack = [int(input()) for _ in range(K)]

jams.sort()
knapsack.sort()

pq = []

idx = 0
res = 0

for sack in knapsack:
    while idx < len(jams) and sack >= jams[idx][0]:
        heapq.heappush(pq, [-jams[idx][1], jams[idx][0]])
        idx += 1
    
    res -= heapq.heappop(pq)[0]

print(res)
    
