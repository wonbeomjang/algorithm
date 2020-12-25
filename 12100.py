from sys import stdin
import copy

input = stdin.readline

def shift(direction):
    # 왼쪽
    if direction == 0:
        for i in range(N):
            index = 0
            for j in range(1, N):
                if board[i][j]:
                    data = board[i][j]
                    board[i][j] = 0
                    
                    if board[i][index] == 0:
                        board[i][index] = data
                    elif board[i][index] == data:
                        board[i][index] = data * 2
                        index += 1
                    else:
                        index += 1
                        board[i][index] = data
                    
    # 오른쪽
    elif direction == 1:
        for i in range(N):
            index = N - 1
            for j in range(N - 2, -1, -1):
                if board[i][j]:
                    data = board[i][j]
                    board[i][j] = 0
                    
                    if board[i][index] == 0:
                        board[i][index] = data
                    elif board[i][index] == data:
                        board[i][index] = data * 2
                        index -= 1
                    else:
                        index -= 1
                        board[i][index] = data
    
    # 위쪽
    elif direction == 2:
        for j in range(N):
            index = 0
            for i in range(1, N):
                if board[i][j]:
                    data = board[i][j]
                    board[i][j] = 0
                    
                    if board[index][j] == 0:
                        board[index][j] = data
                    elif board[index][j] == data:
                        board[index][j] = data * 2
                        index += 1
                    else:
                        index += 1
                        board[index][j] = data
    
    # 아래족
    else:
        for j in range(N):
            index = N - 1
            for i in range(N - 2, -1, -1):
                if board[i][j]:
                    data = board[i][j]
                    board[i][j] = 0
                    
                    if board[index][j] == 0:
                        board[index][j] = data
                    elif board[index][j] == data:
                        board[index][j] = data * 2
                        index -= 1
                    else:
                        index -= 1
                        board[index][j] = data
                    
def print_map(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
                
def dfs(cnt):
    global board, ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, board[i][j]) 
        return
    
    copy_board = copy.deepcopy(board)
    for i in range(4):
        shift(i)
        dfs(cnt + 1)
        
        board = copy.deepcopy(copy_board)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0

dfs(0)
print(ans)
