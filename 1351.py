import sys

input = lambda: sys.stdin.readline().strip()

N, P, Q = map(int, input().split())

dp = {}
dp[0] = 1

def dfs(n):
    global dp, P, Q
    if n in dp[n]:
        return dp[n]
        
    dp[n] = dfs(n // P) + dfs(n // Q)
    
    return dp[n]
    
print(dfs(N))