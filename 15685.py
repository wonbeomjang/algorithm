import sys

input = lambda: sys.stdin.readline().strip()
dxdy = [(1, 0), (0, -1), (-1, 0), (0, 1)]

num_dragon_curve = int(input())

def next_gen(dragon):
    x, y = dragon[-1]
    append_x, append_y = dragon[-1]
    
    for i in range(len(dragon) - 2, -1, -1):
        prev_x, prev_y = dragon[i]
        
        dx = x - prev_x
        dy = y - prev_y
        
        dragon += [(append_x + dy, append_y - dx)]
        
        append_x, append_y = dragon[-1]
        x, y = prev_x, prev_y
        
    return dragon

def count_square(dragons):
    positions = set()
    cnt = 0
    
    for dragon in dragons:
        positions.update(dragon)
        
    for x, y in positions:
        
        if (x + 1, y) in positions and (x, y + 1) in positions and (x + 1, y + 1) in positions:
            cnt += 1
            
    return cnt
    

dragons = []

for i in range(num_dragon_curve):
    x, y, d, g = map(int, input().split())
    dragon = [(x, y), (x + dxdy[d][0], y + dxdy[d][1])]
    
    for i in range(g):
        next_gen(dragon)
        
    dragons += [dragon]

cnt = count_square(dragons)
print(cnt)

