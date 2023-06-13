import sys


input = lambda: sys.stdin.readline().strip()

num_buildings = int(input())
buildings = list(map(int, input().split()))

answer = float("-inf")
for cur_building in range(num_buildings):
    cnt = 0

    max_slop = float("-inf")
    for target_building in range(cur_building + 1, num_buildings):
        slop = (buildings[target_building] - buildings[cur_building]) / (target_building - cur_building)
        if max_slop < slop:
            max_slop = slop
            cnt += 1

    min_slop = float("inf")
    for target_building in range(cur_building - 1, -1, -1):
        slop = (buildings[target_building] - buildings[cur_building]) / (target_building - cur_building)
        if min_slop > slop:
            min_slop = slop
            cnt += 1

    answer = max(answer, cnt)

print(answer)