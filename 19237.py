import sys

input = lambda: sys.stdin.readline().strip()
drdc = ((-1, 0), (1, 0), (0, -1), (0, 1))

UP    = 0
DOWN  = 1
LEFT  = 2
RIGHT = 3

n, num_shark, duration = map(int, input().split())
check = set([i for i in range(num_shark)])

board = [[[0, 0] for i in range(n)] for i in range(n)]
shark = [[] for i in range(num_shark)]
priority = [[[] for _ in range(4)] for _ in range(num_shark)]
check = set([i for i in range(num_shark)])

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j]:
            board[i][j] = [temp[j], duration]
            shark[temp[j] - 1] = [i, j]


temp = list(map(int, input().split()))
for i in range(num_shark):
    shark[i] += [temp[i] - 1]


for i in range(num_shark):
    for j in range(4):
        temp = list(map(int, input().split()))
        for d in temp:
            priority[i][j] += [d - 1]
            
def print_board(board, index=0):
    print()
    for i in range(n):
        for j in range(n):
            print(f'{board[i][j][index]:3}', end='')
        print()

def move(board, shark):
    global check
    
    temp_board = [[0] * n for i in range(n)]
    
    # 작은 번호가 밀어내기 때문에 큰 번호부터
    for i in range(num_shark - 1, -1, -1):
        if not i in check:
            continue
        
        row, col, direction = shark[i]
        
        flag = False
        
        for j in range(4):
            next_direction = priority[i][direction][j]
            next_row = row + drdc[next_direction][0]
            next_col = col + drdc[next_direction][1]
            
            # 냄새가 안나면
            if (0 <= next_row < n and 0 <= next_col < n) and not board[next_row][next_col][1]:
                flag = True
                break
            
        if not flag:
            for j in range(4):
                next_direction = priority[i][direction][j]
                next_row = row + drdc[next_direction][0]
                next_col = col + drdc[next_direction][1]
                
                # 자기냄새라면
                if (0 <= next_row < n and 0 <= next_col < n) and board[next_row][next_col][0] == i + 1:
                    break
        
        temp_board[next_row][next_col] = [i + 1, duration]
        shark[i] = [next_row, next_col, next_direction]
    
    # 냄새 줄어들기
    for i in range(n):
        for j in range(n):
            if board[i][j][1]:
                board[i][j][1] -= 1
                if not board[i][j][1]:
                    board[i][j] = [0, 0]
                    
    
    check.clear()
    
    for i in range(n):
        for j in range(n):
            if temp_board[i][j]:
                check.add(temp_board[i][j][0] - 1)
                board[i][j] = temp_board[i][j]

ans = 0

for i in range(1000):
    for i in range(1, num_shark):
        if i in check:
            break
    else:
        print(ans)
        break
    
    ans += 1
    move(board, shark)
else:
    print(-1)
            
            
        