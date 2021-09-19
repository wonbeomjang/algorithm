import sys

input = lambda: sys.stdin.readline().strip()
drdc = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

n, num_fireballs, num_commands = map(int, input().split())
board = [[[] for i in range(n)] for i in range(n)]

fireballs = []
for i in range(num_fireballs):
    row, col, mass, speed, direction = map(int, input().split())
    board[row - 1][col - 1] += [[mass, speed, direction]]


def move():
    global board
    temp_board = [[[] for i in range(n)] for i in range(n)]
    
    # 이동
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for (mass, speed, direction) in board[i][j]:
                    next_row = (i + speed * drdc[direction][0]) % n
                    next_col = (j + speed * drdc[direction][1]) % n
                    
                    temp_board[next_row][next_col] += [[mass, speed, direction]]
                    
    
    # 합치기
    for i in range(n):
        for j in range(n):
            if len(temp_board[i][j]) > 1:
                total_mass, total_speed, next_direction = 0, 0, 0
                cnt = len(temp_board[i][j])
                
                for (mass, speed, direction) in temp_board[i][j]:
                    total_mass += mass
                    total_speed += speed
                    next_direction += (direction) % 2
                    
                # 나누기
                mass = int(total_mass / 5)
                speeed = int(total_speed / cnt)
                directions = (0, 2, 4, 6) if (next_direction == 0 or next_direction == cnt) else (1, 3, 5, 7)
                
                temp_board[i][j] = []
                if mass:
                    for d in directions:
                        
                        temp_board[i][j] += [[mass, speeed, d]]
                
    board = temp_board
    

        
for i in range(num_commands):
    move()

ans = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            ans += sum((b[0] for b in board[i][j]))

print(ans)