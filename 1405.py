from itertools import combinations

num, E, W, S, N = map(int, input().split())
porbs = [E / 100, W / 100, S / 100, N / 100]
dxdy = [(1, 0), (-1, 0), (0, -1), (0, 1)]

ans = 0

def dfs(x, y, prob, num_step, visited):
    global num
    global ans
    
    if num_step == num:
        ans += prob
        return
    
    for i, (dx, dy) in enumerate(dxdy):
        next_x = x + dx
        next_y = y + dy
        
        if not (next_x, next_y) in visited:
            visited += [(next_x, next_y)]
            dfs(next_x, next_y, prob * porbs[i], num_step + 1, visited)
            visited.pop()

dfs(0, 0, 1, 0, [(0, 0)])
print(ans)