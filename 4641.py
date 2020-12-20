from sys import stdin, stdout

wb = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
bw = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

map1 = [wb, bw, wb, bw, wb, bw, wb, bw]

def calc(m, start_i, start_j):
    global map1
    cnt = 0
    
    for i in range(8):
        for j in range(8):
            if map1[i][j] != m[start_i + i][start_j + j]:
                cnt += 1
    
    cnt = min(cnt, 64 - cnt)
    
    return cnt

n, m = map(int, stdin.readline().split())

total_map = []

for i in range(n):
    total_map += [list(stdin.readline())]

ans = n * m



for i in range(n - 7):
    for j in range(m - 7):
        ans = min(ans, calc(total_map, i, j))
        
print(ans)