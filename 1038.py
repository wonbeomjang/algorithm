from itertools import combinations
from sys import stdin, stdout

elements = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
decr = []
for i in range(1, 11):
    for element in combinations(elements, i):
        decr += [int(''.join(element))]
        
decr.sort()

N = int(stdin.readline())

if N < 1023:
    stdout.write(f'{decr[N]}')
else:
    stdout.write('-1')