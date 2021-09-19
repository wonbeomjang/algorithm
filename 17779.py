import sys

input = lambda: sys.stdin.readline().strip()

def make_sector(x, y, d1, d2):
    global sector
    
    for i in range(d1 + 1):
        sector[x + i][y - i] = 5
        sector[x + d2 + i][y + d2 - i] = 5
    
    for i in range(d2 + 1):
        sector[x + i][y + i] = 5
        sector[x + d1 + i][y - d1 + i] = 5
    
    for i in range(n):
        index = [i for i, x in enumerate(sector[i]) if x == 5]
        if len(index) > 1:
            for j in range(*index):
                sector[i][j] = 5
    
    for r in range(n):
        for c in range(n):
            if sector[r][c]: continue
            elif 0 <= r < x + d1 and 0 <= c <= y: sector[r][c] = 1
            elif 0 <= r <= x + d2 and y < c < n: sector[r][c] = 2
            elif x + d1 <= r < n and 0 <= c < y - d1 + d2: sector[r][c] = 3
            elif x + d2 < r < n and y - d1 + d2 <= c < n: sector[r][c] = 4
                
    
def get_population():
    global sector, board
    
    people = [0] * 5
    
    for i in range(n):
        for j in range(n):
            people[sector[i][j] - 1] += board[i][j]
    
    return people

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
result = float('inf')

for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if 0 <= x < x + d1 + d2 < n and 0 <= y - d1 < y < y + d2 < n:
                    sector = [[0] * n for i in range(n)]
                    
                    make_sector(x, y, d1, d2)
                    people = sorted(get_population())
                    result = min(result, people[-1] - people[0])

print(result)