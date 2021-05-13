N = int(input())

nums = [int(input()) for _ in range(N)]

positive = []
negative = []

ans = 0

for n in nums:
    if n == 1:
        ans += 1
    elif n > 1:
        positive += [n]
    else:
        negative += [n]

negative.sort()
positive.sort(reverse=True)

for i in range(0, len(positive), 2):
    if i + 1 < len(positive):
        ans += positive[i] * positive[i + 1]
    else:
        ans += positive[i]

for i in range(0, len(negative), 2):
    if i + 1 < len(negative):
        ans += negative[i] * negative[i + 1]
    else:
        ans += negative[i]

print(ans)