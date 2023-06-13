from collections import defaultdict

num_row, num_col = map(int, input().split())
lamp_count = defaultdict(int)
for i in range(num_row):
    lamp_count[tuple(map(int, list(input())))] += 1

max_click = int(input())

answer = 0
for i in range(max_click % 2, min(max_click, num_col) + 1, 2):
    for k in lamp_count:
        if sum(k) + i == num_col:
            answer = max(answer, lamp_count[k])

print(answer)