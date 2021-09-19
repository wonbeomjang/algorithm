import sys

input = lambda: sys.stdin.readline().strip()

move = [0] * 33
score = [0] * 33
jump = {}
check = [0] * 33

for i in range(32):
    move[i] = i + 1

move[21] = 21
move[22], move[23], move[24] = 23, 24, 30
move[25], move[26] = 26, 30
move[32] = 20

for i in range(32):
    score[i] = i * 2

score[21] = 0
score[22], score[23], score[24] = 13, 16, 19
score[25], score[26] = 22, 24
score[27], score[28], score[29] = 28, 27, 26
score[30], score[31], score[32] = 25, 30, 35

jump[5], jump[10], jump[15] = 22, 25, 27

positions = [0] * 4

dices = list(map(int, input().split()))

max_ans = 0
def dfs(index, ans):
    global max_ans
    if index == 10:
        max_ans = max(max_ans, ans)
        return
    
    for i in range(4):
        temp, pos, dice = positions[i], positions[i], dices[index]
        
        if pos in jump:
            pos = jump[pos]
            dice -= 1
        
        if pos + dice <= 21:
            pos += dice
        else:
            for _ in range(dice):
                pos = move[pos]
                
        if pos != 21 and check[pos]:
            continue
        
        check[pos], check[temp], positions[i] = 1, 0, pos
        dfs(index + 1, ans + score[pos])
        check[pos], check[temp], positions[i] = 0, 1, temp
        
dfs(0, 0)
print(max_ans)