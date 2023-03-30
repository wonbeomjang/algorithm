from itertools import combinations
import sys

input = lambda: sys.stdin.readline().strip()


cnt = 0

T = int(input())

for i in range(T):
    num_point = int(input())
    point = [tuple(map(int, input().split())) for i in range(num_point)]
    answer = float('inf')

    for start_points in combinations(range(num_point), num_point // 2):
        start_points = set(start_points)

        x = 0
        y = 0

        for i in range(num_point):
            if i in start_points:
                x += point[i][0]
                y += point[i][1]
            else:
                x -= point[i][0]
                y -= point[i][1]

        answer = min(answer, (x*x+y*y)**0.5)
    print(answer)


