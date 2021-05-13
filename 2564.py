NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

num_col, num_row = map(int, input().split())
num_store = int(input())

total_dis = (num_row + num_col) * 2

def calc(dir, dis):
    global num_col, num_row
    
    res = 0
    if dir == NORTH: res = dis
    elif dir == EAST: res = num_col + dis
    elif dir == SOUTH: res = num_col + num_row + (num_col - dis)
    else: res = num_col + num_row + num_col + (num_row - dis)
        
    return res

stores = []

for _ in range(num_store):
    stores += [calc(*list(map(int, input().split())))]

start = calc(*list(map(int, input().split())))

res = 0

for store in stores:
    dis = abs(store - start)
    res += min(dis, total_dis - dis)

print(res)