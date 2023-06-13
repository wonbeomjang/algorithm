import collections
import math
import sys

input = lambda: sys.stdin.readline().strip()


n = int(input())
node = collections.defaultdict(lambda: 1)
edge = collections.defaultdict(list)


def bfs(n, w, v):
    node[n] *= w
    for m in edge[n]:
        if m not in v:
            v.add(m)
            bfs(m, w, v)

for i in range(n - 1):
    v1, v2, w1, w2 = map(int, input().split())

    w1 = w1 * node[v2]
    w2 = w2 * node[v1]

    g = math.gcd(w1, w2)
    w1 //= g
    w2 //= g

    bfs(v1, w1, {v1})
    bfs(v2, w2, {v2})

    edge[v1] += [v2]
    edge[v2] += [v1]

res = []
for i in range(n):
    res += [node[i]]

divider = math.gcd(*res)
for i in range(n):
    res[i] //= divider

print(" ".join(map(str, res)))