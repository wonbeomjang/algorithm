from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.extend([[x, y, 0], [x, y, 1], [x, y, 2], [x, y, 3]])
    c[x][y] = [1, 1, 1, 1]
    ans = []
    while q:
        x, y, dir = q.popleft()
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < h and 0 <= ny < w:
            if not c[nx][ny][dir] or c[nx][ny][dir] > c[x][y][dir]:
                if a[nx][ny] == '.':
                    c[nx][ny][dir] = c[x][y][dir]
                    q.appendleft([nx, ny, dir])
                    turn(nx, ny, dir)
                elif nx == x2 and ny == y2:
                    c[nx][ny][dir] = c[x][y][dir]
                    ans.append(c[nx][ny][dir])

    print(min(ans)-1)

def turn(x, y, dir):
    ndir = [(dir + 1) % 4, (dir + 3) % 4]
    for k in ndir:
        if not c[x][y][k] or c[x][y][k] > c[x][y][dir] + 1:
            c[x][y][k] = c[x][y][dir] + 1
            q.append([x, y, k])

w, h = map(int, input().split())

a, temp = [], []
for i in range(h):
    row = list(input().strip())
    a.append(row)
    for j, k in enumerate(row):
        if a[i][j] == 'C':
            temp.extend([i, j])
x1, y1, x2, y2 = temp

q = deque()
c = [[[0]*4 for _ in range(w)] for _ in range(h)]
bfs(x1, y1)