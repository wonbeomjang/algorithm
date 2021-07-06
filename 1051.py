import sys

input = lambda: sys.stdin.readline().strip()

num_row, num_col = map(int, input().split())

board = [list(input()) for i in range(num_row)]

ans = 0

for i in range(num_row):
    for j in range(num_col):
        for k in range(min(num_row, num_col)):
            try:
                if board[i][j] == board[i + k][j] == board[i][j + k] == board[i + k][j + k]:
                    ans = max(ans, k + 1)
                
            except:
                pass
            
print(ans * ans)