req = [1, 1, 2, 2, 2, 8]
cur = list(map(int, input().split()))
for i, r in enumerate(req):
    print(r - cur[i], end=' ')