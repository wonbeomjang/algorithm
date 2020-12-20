from sys import stdin, stdout
from itertools import combinations

height = []

for _ in range(9):
    height += [int(stdin.readline())]

height.sort()

summation = sum(height) - 100

for n1, n2 in combinations(height, 2):
    if n1 + n2 == summation:
        height.remove(n1)
        height.remove(n2)

for h in height:
    stdout.write(f'{h}\n')