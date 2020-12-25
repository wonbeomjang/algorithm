import sys
input = sys.stdin.readline

N = int(input())

dp = [-1 for i in range(100000)]

cost = [list(map(int, input().split())) for i in range(N)]
on = list(input()[:-1])
P = int(input())

def dfs(state, cnt):
    global cost, ans
    
    if cnt == P:
        return 0
    cur_cost = dp[state]  
    
    if cur_cost != -1:
        return cur_cost
    
    cur_cost = float('inf')
    
    for i in range(N):
        # i가 안켜져있으면
        if not ((1 << i) & state):
            for j in range(N):
                if i == j:
                    continue
                
                if ((1 << j) & state):
                    cur_cost = min(cur_cost, dfs(state | (1 << i), cnt + 1) + cost[j][i])
    return cur_cost

state = 0
for i in range(N):
    if on[i] == 'Y':
        P -= 1
        state |= (1 << i)
        
ans = dfs(state, 0)

if (P <= 0):
    print(0)
elif ans == float('inf'):
    print(-1)
else:
    print(ans)