import sys

input = lambda: sys.stdin.readline().strip()

num_levels = int(input())

scores = []
for _ in range(num_levels):
    scores += [int(input())]

last_score = 100000
res = 0

for score in reversed(scores):
    if not score < last_score:
        res += score - last_score + 1
        last_score = score - 1
    else:
        last_score = score
        
print(res)
        