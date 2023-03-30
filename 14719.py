num_row, num_col = map(int, input().split())

wall = list(map(int, input().split()))
water = 0

for i in range(1, len(wall) - 1):
    water += max(min(max(wall[:i]), max(wall[i+1:])) - wall[i], 0)

print(water)