from sys import stdin, stdout
from itertools import combinations

N = int(stdin.readline())

nums = list(range(10))

decending_num = []

for i in range(1, 11):
    for n in combinations(nums, i):
        n = sorted(list(n), reverse=True)
        n = map(str, n)
        decending_num += [''.join(n)]
decending_num = list(map(int, decending_num))
decending_num.sort()
decending_num = list(map(str, decending_num))

if N < 1024:
    stdout.write(f'{decending_num[N - 1]}')
else:
    stdout.write('-1')