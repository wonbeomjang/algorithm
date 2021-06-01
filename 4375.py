import sys
import re

input = lambda: sys.stdin.readline().strip()

num_test = int(input())
pattern = re.compile('1+')

for _ in range(num_test):
    res = 1
    num = int(input())
    i = 1
    while True:
        res = i * num
        if pattern.match(f'{res}'):
            print(len(f'{res}'), res)
            break
        i += 1