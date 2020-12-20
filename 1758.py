from sys import stdin, stdout

n = int(stdin.readline())

tips = []

for i in range(n):
    tip = int(stdin.readline())
    tips += [tip]

tips.sort(reverse=True)

summation = 0
for i, tip in enumerate(tips):
    if tip - i < 0:
        continue
    summation += tip - i

print(summation)
