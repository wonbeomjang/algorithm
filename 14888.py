import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))
num_plus, num_minus, num_multiply, num_division = map(int, input().split())

max_num = 0
min_num = float('inf')

def dfs(pos, num_plus, num_minus, num_multiply, num_division, res):
    global min_num, max_num
    if pos == n:
        min_num = min(min_num, res)
        max_num = max(max_num, res)
        return
    
    if num_plus:     dfs(pos + 1, num_plus - 1, num_minus, num_multiply, num_division, res + arr[pos])
    if num_minus:    dfs(pos + 1, num_plus, num_minus - 1, num_multiply, num_division, res - arr[pos])
    if num_multiply: dfs(pos + 1, num_plus, num_minus, num_multiply - 1, num_division, res * arr[pos])
    if num_division: dfs(pos + 1, num_plus, num_minus, num_multiply, num_division - 1, int(res / arr[pos]))
    
dfs(1, num_plus, num_minus, num_multiply, num_division, arr[0])
print(max_num)
print(min_num)