import sys

input = lambda: sys.stdin.readline().strip()
move = ((0, -1), (1, 0), (0, 1), (-1, 0))
drdc = ((-1, 0), (1, 0), (0, -1), (0, 1))

n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
commands = []

for i in range(m):
    dir, dis = map(int, input().split())
    commands += [(dir - 1, dis)]
    
    
marbles = []

def print_board():
    print()
    for i in range(n):
        for j in range(n):
            print(f'{board[i][j]:3}', end='')
        print()

def set_marble():
    global marbles
    temp = []
    row = col = n // 2
    
    dis = 1
    while True:
        for i in range(4):
            for _ in range(dis):
                row += move[i][0]
                col += move[i][1]
                
                if row == col == 0:
                    marbles = temp
                    return
                
                if board[row][col]:
                    temp += [board[row][col]]
                    
            if i == 1 or i == 3:
                dis += 1
    
    marbles = temp

def blizzard(dir, dis):
    row = col = n // 2
    
    for i in range(dis):
        row += drdc[dir][0]
        col += drdc[dir][1]
        
        board[row][col] = 0
    
    set_marble()

def set_board():
    global board, marbles
    row = col = n // 2
    temp = [[0] * n for i in range(n)]
    
    i = 0
    dis = 1
    while True:
        for d in range(4):
            for _ in range(dis):
                row += move[d][0]
                col += move[d][1]
                
                temp[row][col] = marbles[i]
                i += 1
                
                if row == col == 0 or i >= len(marbles):
                    board = temp
                    return
                    
            if d == 1 or d == 3:
                dis += 1

def explosion():
    global marbles
    temp = []
    score = 0
    
    s = e = 0
    
    while s < len(marbles):
        while e < len(marbles) and marbles[s] == marbles[e]: e += 1
    
        if e - s >= 4:
            score += marbles[s] * (e - s)
        else:
            for k in range(s, e):
                temp += [marbles[k]]
            
        s = e
        
    marbles = temp
    
    return score

def change():
    global marbles
    
    temp = []
    
    s = e = 0
    while s < len(marbles):
        if len(temp) >= n * n: break
    
        while e < len(marbles) and marbles[s] == marbles[e]: e += 1
        temp += [e - s, marbles[s]]
        s = e
        
    marbles = temp[:n*n - 1]

for dir, dis in commands:
    blizzard(dir ,dis)
    
    total = 0
    while True:
        score = explosion()
        if not score: break
        total += score
        
    change()
    set_board()
    
    print_board()
    print(marbles)
print(total)
    