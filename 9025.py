import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().strip()
dxdy = ((1, 0), (0, 1), (-1, 0), (0, -1))

num_test = int(input())


def bfs(home_coord, shop_coord, target_coord):
    q = deque([home_coord])
    visited = set(home_coord)

    while q:
        x, y = q.popleft()

        if abs(x - target_coord[0]) + abs(y - target_coord[1]) <= 1000:
            return "happy"

        for shop_x, shop_y in shop_coord:
            if (shop_x, shop_y) in visited:
                continue

            if abs(x - shop_x) + abs(y - shop_y) <= 1000:
                q.append((shop_x, shop_y))
                visited.add((shop_x, shop_y))

    return "sad"


for _ in range(num_test):
    num_shops = int(input())

    home_coord = tuple(map(int, input().split()))
    shop_coord = set([tuple(map(int, input().split())) for i in range(num_shops)])
    target_coord = tuple(map(int, input().split()))

    print(bfs(home_coord, shop_coord, target_coord))

