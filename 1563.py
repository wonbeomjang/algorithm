import sys

sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline().strip()

N = int(input())
dp = {}


def dfs(n, num_late, num_absent):
    global N
    if num_late > 1 or num_absent > 2:
        return 0
        
    if n == N:
        return 1
        
    if not (n, num_late, num_absent) in dp:
        ans = dfs(n + 1, num_late + 1, 0) + dfs(n + 1, num_late, num_absent + 1) + dfs(n + 1, num_late, 0)
        dp[(n, num_late, num_absent)] = ans % 1000000
    
    return dp[(n, num_late, num_absent)] % 1000000

print(dfs(0, 0, 0) % 1000000)