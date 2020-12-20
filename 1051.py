from sys import stdin

n, m = map(int, stdin.readline().split())
rec = []
for _ in range(n):
    rec += [list(stdin.readline())]
    
res = 0

for i in range(n):
    for j in range(m):
        for k in range(min(m, n)):
            if i + k < n and j + k < m and rec[i + k][j] == rec[i][j] and rec[i + k][j + k] == rec[i][j] and rec[i][j + k] == rec[i][j]:
                res = max(res, (k + 1) * (k + 1))
                
print(res)
                